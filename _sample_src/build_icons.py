#!/usr/bin/env python3
"""카메라 웹 UI 실제 아이콘(img/*.png, jQuery UI 스프라이트) → icm/images/icons/*.png (24x24)
usage: build_icons.py <카메라 www 루트 (예: icm/package-enx/.temp/rootfs_app/www)>"""
import os, sys
from PIL import Image

WWW = sys.argv[1]
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icm", "images", "icons")
os.makedirs(OUT, exist_ok=True)

FILES = {  # 출력 이름: www/img 파일
    "logout": "to_logout.png", "live": "live.png", "ai": "ai.png", "setup": "setup.png",
    "menu": "menu-show-hide.png", "motion": "motion_off.png",
    "zoom_in": "zoom-in.png", "zoom_out": "zoom-out.png", "auto_focus": "auto-focus.png",
    "save": "save.png", "add": "add.png", "grid": "grid.png",
    "drag_select": "drag_lt_rb.png", "drag_deselect": "drag_rb_lt.png",
}
SPRITES = {  # 출력 이름: (스프라이트 색, background-position x, y) — 화면과 같은 색
    "snapshot": ("777777", -208, -128), "fullscreen": ("777777", 0, -80),
    "focus_plus": ("777777", -16, -128), "focus_minus": ("777777", -48, -128),
    "ptz_zoom_in": ("777777", -128, -112), "ptz_zoom_out": ("777777", -144, -112),
    "reboot": ("444444", 0, -176), "default": ("444444", 0, -64), "reset": ("777777", 0, -64),
    "upload": ("444444", -192, -48), "download": ("444444", -224, -48),
    "move_up": ("777777", 0, -48), "move_left": ("777777", -96, -48),
    "move_right": ("777777", -32, -48), "move_down": ("777777", -64, -48),
    "size_up": ("777777", -192, -48), "size_left": ("777777", -240, -48),
    "size_right": ("777777", -208, -48), "size_down": ("777777", -224, -48),
    "event_log": ("777777", -128, -96), "roi_all": ("777777", -16, -80),
    "roi_edit": ("777777", -64, -112), "roi_save": ("777777", -96, -112),
}

def put(name, icon):
    icon = icon.convert("RGBA")
    if max(icon.size) > 24:
        icon = icon.resize((24, 24), Image.LANCZOS)
    c = Image.new("RGBA", (24, 24), (0, 0, 0, 0))
    c.paste(icon, ((24 - icon.width) // 2, (24 - icon.height) // 2), icon)
    c.save(os.path.join(OUT, name + ".png"))

for n, f in FILES.items():
    put(n, Image.open(os.path.join(WWW, "img", f)))
for n, (col, x, y) in SPRITES.items():
    sp = Image.open(os.path.join(WWW, "css", "images", f"ui-icons_{col}_256x240.png"))
    put(n, sp.crop((-x, -y, -x + 16, -y + 16)))
print(len(FILES) + len(SPRITES), "icons")
