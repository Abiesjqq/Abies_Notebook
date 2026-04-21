import json
import time
import urllib.request
import urllib.error
import webbrowser
import winsound
import ctypes
from datetime import datetime

MANIFEST_URL = "https://launchermeta.mojang.com/mc/game/version_manifest_v2.json"
TARGET_VERSION = "26.1"
CHECK_INTERVAL = 30


def fetch_manifest():
    req = urllib.request.Request(
        MANIFEST_URL,
        headers={
            "User-Agent": "Mozilla/5.0",
            "Cache-Control": "no-cache"
        }
    )
    with urllib.request.urlopen(req, timeout=10) as resp:
        return json.loads(resp.read().decode())


def check_release(manifest):
    latest = manifest.get("latest", {}).get("release")

    for v in manifest.get("versions", []):
        if v.get("id") == TARGET_VERSION:
            return True, latest, v

    return False, latest, None


def notify(info):
    msg = (
        f"Minecraft {TARGET_VERSION} 已发布！\n\n"
        f"发布时间: {info.get('releaseTime')}\n"
    )

    # 声音提示
    for _ in range(3):
        winsound.Beep(1200, 200)
        time.sleep(0.1)

    # 弹窗
    ctypes.windll.user32.MessageBoxW(
        0,
        msg,
        "MC 更新提醒",
        0x40
    )

    # 打开页面（可删）
    webbrowser.open("https://www.minecraft.net/en-us/articles")


def main():
    print(f"监控版本: {TARGET_VERSION}")
    print(f"间隔: {CHECK_INTERVAL} 秒")
    print("-" * 40)

    while True:
        now = datetime.now().strftime("%H:%M:%S")

        try:
            manifest = fetch_manifest()
            found, latest, info = check_release(manifest)

            if found or latest == TARGET_VERSION:
                print(f"[{now}] ✅ 已发布！")
                notify(info)
                break

            print(f"[{now}] 未发布 | latest = {latest}")

        except Exception as e:
            print(f"[{now}] ⚠ 错误: {e}")

        time.sleep(CHECK_INTERVAL)


if __name__ == "__main__":
    main()