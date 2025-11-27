from pathlib import PurePosixPath

# Track bilingual page pairs
# key: (dir_path, base_name) -> {"default": file (English), "zh": file}
_LANG_PAIRS = {}

def _analyze_file(file):
    """Identify language and base filename for a markdown file."""
    src = PurePosixPath(file.src_path)
    name = src.name

    # Only handle markdown files
    if not name.endswith(".md"):
        return None

    if name.endswith(".zh.md"):
        stem = name[:-len(".zh.md")]
        base_name = f"{stem}.md"  # Align with the default filename like xxx.md
        lang = "zh"
    else:
        base_name = name
        lang = "default"  # default = English

    key = (str(src.parent), base_name)
    return key, lang


def on_files(files, config):
    """Collect bilingual pairs when scanning all files."""
    global _LANG_PAIRS
    _LANG_PAIRS = {}

    for f in files:
        info = _analyze_file(f)
        if info is None:
            continue

        key, lang = info
        bucket = _LANG_PAIRS.setdefault(key, {})
        bucket[lang] = f

    return files


def on_page_markdown(markdown, page, config, files):
    """Inject a language switcher before rendering markdown."""
    info = _analyze_file(page.file)
    if info is None:
        return markdown

    key, lang = info
    pair = _LANG_PAIRS.get(key)

    if not pair or "default" not in pair or "zh" not in pair:
        return markdown

    if lang == "zh":
        this_label = "中文"
        other_label = "English"
        other_file = pair["default"]
    else:
        this_label = "English"
        other_label = "中文"
        other_file = pair["zh"]

    # Use absolute URL to avoid duplicated segments when nested paths are rendered
    other_url = "/" + other_file.url.lstrip("/")

    switcher_html = f"""
<div class="lang-switch">
  <span class="lang-current">{this_label}</span>
  <a class="lang-other" href="{other_url}">{other_label}</a>
</div>
"""

    return switcher_html + "\n\n" + markdown
