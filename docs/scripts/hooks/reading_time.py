import re
from functools import lru_cache

# 预编译正则表达式
CHINESE_CHARS_PATTERN = re.compile(r'[\u4e00-\u9fff\u3400-\u4dbf]')
ENGLISH_WORD_PATTERN = re.compile(r'\b[a-zA-Z]{2,}\b')
CODE_BLOCK_PATTERN = re.compile(r'```.*?```', re.DOTALL)
INLINE_CODE_PATTERN = re.compile(r'`[^`]+`')
YAML_FRONT_PATTERN = re.compile(r'^---.*?---\s*', re.DOTALL)
HTML_TAG_PATTERN = re.compile(r'<[^>]+>')
IMAGE_PATTERN = re.compile(r'!\[.*?\]\([^)]+\)')
LINK_PATTERN = re.compile(r'\[([^\]]+)\]\([^)]+\)')

@lru_cache(maxsize=256)
def clean_markdown_content_for_reading(content_hash, markdown):
    content = markdown
    content = YAML_FRONT_PATTERN.sub('', content)
    content = HTML_TAG_PATTERN.sub('', content)
    content = IMAGE_PATTERN.sub('', content)
    content = LINK_PATTERN.sub(r'\1', content)
    content = CODE_BLOCK_PATTERN.sub('', content)
    content = INLINE_CODE_PATTERN.sub('', content)
    return content

def count_code_lines(markdown):
    code_blocks = CODE_BLOCK_PATTERN.findall(markdown)
    total_code_lines = 0
    for block in code_blocks:
        code_content = re.sub(r'^```\w*\n?', '', block)
        code_content = re.sub(r'\n?```$', '', code_content)
        if not code_content.strip():
            continue
        lines = [line for line in code_content.split('\n') if line.strip()]
        total_code_lines += len(lines)
    return total_code_lines

def count_images(markdown):
    return len(IMAGE_PATTERN.findall(markdown))

def count_headings(markdown):
    return len(re.findall(r'^#+\s', markdown, flags=re.MULTILINE))

def count_tables(markdown):
    return len(re.findall(r'\n\|.*\|', markdown))

def calculate_reading_stats(markdown):
    content_hash = hash(markdown)
    clean_content = clean_markdown_content_for_reading(content_hash, markdown)
    chinese_chars = len(CHINESE_CHARS_PATTERN.findall(clean_content))
    english_words = len(ENGLISH_WORD_PATTERN.findall(clean_content))
    code_lines = count_code_lines(markdown)
    image_count = count_images(markdown)
    heading_count = count_headings(markdown)
    table_count = count_tables(markdown)

    chinese_minutes = chinese_chars / 400
    english_minutes = english_words / 200
    code_minutes = code_lines / 50
    image_minutes = image_count * 0.2
    heading_minutes = heading_count * 0.1
    table_minutes = table_count * 0.3

    total_minutes = max(1, round(
        chinese_minutes + english_minutes + code_minutes + image_minutes + heading_minutes + table_minutes
    ))

    return total_minutes, chinese_chars, code_lines

def on_page_markdown(markdown, **kwargs):
    page = kwargs['page']
    if page.meta.get('hide_reading_time', False):
        return markdown

    EXCLUDE_PATTERNS = [
        re.compile(r'^index\\.md$'),
        re.compile(r'^trip/index\\.md$'),
        re.compile(r'^relax/index\\.md$'),
        re.compile(r'^blog/indexblog\\.md$'),
        re.compile(r'^blog/posts\\.md$'),
        re.compile(r'^develop/index\\.md$'),
        re.compile(r'waline\\.md$'),
        re.compile(r'link\\.md$'),
        re.compile(r'404\\.md$'),
    ]

    EXCLUDE_TYPES = frozenset({'landing', 'special', 'widget'})

    src_path = page.file.src_path
    for pattern in EXCLUDE_PATTERNS:
        if pattern.match(src_path):
            return markdown

    page_type = page.meta.get('type', '')
    if page_type in EXCLUDE_TYPES:
        return markdown

    if len(markdown) < 300:
        return markdown

    reading_time, chinese_chars, code_lines = calculate_reading_stats(markdown)

    if chinese_chars < 50 and code_lines < 5:
        return markdown

    reading_info = f"""!!! info reading-info \"阅读信息\"
    <span class=\"twemoji\"><svg viewBox=\"0 0 24 24\" xmlns=\"http://www.w3.org/2000/svg\"><path d=\"M12 2A10 10 0 0 0 2 12a10 10 0 0 0 10 10 10 10 0 0 0 10-10h-2a8 8 0 0 1-8 8 8 8 0 0 1-8-8 8 8 0 0 1 8-8V2m6.78 1a.69.69 0 0 0-.48.2l-1.22 1.21 2.5 2.5L20.8 5.7c.26-.26.26-.7 0-.95L19.25 3.2c-.13-.13-.3-.2-.47-.2m-2.41 2.12L9 12.5V15h2.5l7.37-7.38-2.5-2.5Z\"></path></svg></span> 约 **{chinese_chars}** 个字&nbsp;&nbsp;**{reading_time}** 分钟&nbsp;&nbsp;本页总访问量：<span id="busuanzi_value_site_pv">加载中...</span> 次\n\n"""

    return  reading_info + markdown
