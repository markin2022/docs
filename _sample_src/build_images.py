#!/usr/bin/env python3
"""원본 캡처(raw) → 매뉴얼 이미지(png) 생성.
- 영상 영역(rects, CSS px)에 sample.jpg 합성
  mode 'paste'   : 그대로 붙여넣기(검은 배경 라이브 화면)
  mode 'multiply': 흰 배경 위에 그려진 OSD/ROI/모션 그리드를 살리며 합성
- 왼쪽 아래 마우스 커서 지우기
- crop: (x0,y0,x1,y1) 스크린샷 픽셀 기준
"""
import os, sys
from PIL import Image, ImageChops

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "raw")
OUT = os.path.join(HERE, "..", "MI-IPE2525", "images")
IW = 1584  # window.innerWidth (CSS px)
sample = Image.open(os.path.join(HERE, "sample.jpg")).convert("RGB")

# name: (raw file, rects, mode, crop)
JOBS = {
    "login":            ("login_clean.jpg", [], None, None),
    "live":             ("live.jpg", [[319.19, 90.34, 1262, 709.88]], "paste", None),
    "live_ai":          ("live_ai.jpg", [[310.81, 180.27, 947.38, 532.90]], "paste", None),
    "sys_info":         ("sys_info.jpg", [], None, None),
    "sys_manager":      ("sys_manager.jpg", [], None, None),
    "sys_date":         ("sys_date.jpg", [], None, None),
    "sys_user":         ("sys_user.jpg", [], None, None),
    "sys_log":          ("sys_log.jpg", [], None, None),
    "av_video_stream":  ("av_video_stream.jpg", [], None, None),
    "av_video_setup":   ("av_video_setup.jpg", [[339.19, 120.06, 639, 359.44]], "overlay", None),
    "av_camera_setup":  ("av_camera_daynight.jpg", [[630.19, 118.78, 640, 360]], "overlay", None),
    "cam_exposure":     ("cam_exposure.jpg", [], None, (305, 392, 1500, 778)),
    "cam_color":        ("cam_color.jpg", [], None, (305, 318, 1500, 778)),
    "cam_image":        ("cam_image.jpg", [], None, (305, 388, 1500, 778)),
    "cam_wdr":          ("cam_wdr.jpg", [], None, (305, 360, 1500, 778)),
    "cam_daynight":     ("av_camera_daynight.jpg", [], None, (305, 488, 1500, 778)),
    "av_privacy_setup": ("av_privacy_setup.jpg", [[622.69, 119.78, 640, 360]], "overlay", None),
    "sys_ptz":          ("sys_ptz.jpg", [[629.88, 120.78, 640, 360]], "overlay", None),
    "av_osd_setup":     ("av_osd_setup.jpg", [[345.19, 186.61, 499.5, 280.97]], "overlay", None),
    "net_interface":    ("net_interface.jpg", [], None, None),
    "net_port":         ("net_port.jpg", [], None, None),
    "net_upnp":         ("net_upnp.jpg", [], None, None),
    "net_rtsp_onvif":   ("net_rtsp_onvif.jpg", [], None, None),
    "event_motion":     ("event_motion.jpg", [[339.19, 150.06, 639, 359.44]], "multiply", None),
    "event_ai_od":      ("event_ai_od.jpg", [], None, (305, 105, 1500, 800)),
    "event_ai_va":      ("event_ai_va.jpg", [[332.20, 112.78, 639.33, 359.63]], "overlay", None),
    "event_ai_va_cfg":  ("event_ai_va_scrolled.jpg", [], None, (305, 340, 1500, 800)),
}


def erase_cursor(img):
    # 왼쪽 메뉴 배경색으로 커서(약 60,790) 덮기
    if img.height < 800:
        return
    bg = img.getpixel((150, 800))
    for x in range(48, 82):
        for y in range(778, img.height):
            if abs(sum(img.getpixel((x, y))) - sum(bg)) < 60 or True:
                img.putpixel((x, y), bg)


def build(name, raw, rects, mode, crop):
    img = Image.open(os.path.join(RAW, raw)).convert("RGB")
    s = img.width / IW
    for x, y, w, h in rects:
        X, Y, W, H = round(x * s), round(y * s), round(w * s), round(h * s)
        pic = sample.resize((W, H), Image.LANCZOS)
        region = img.crop((X, Y, X + W, Y + H))
        if mode == "multiply":
            pic = ImageChops.multiply(pic, region)
        elif mode == "overlay":
            # 흰 배경(영상 자리)만 사진으로, 그 위 OSD/ROI 선은 유지
            mask = region.convert("L").point(lambda v: 255 if v >= 235 else 0)
            pic = Image.composite(pic, region, mask)
        img.paste(pic, (X, Y))
    if not crop and name not in ("login",):
        erase_cursor(img)
    if crop:
        img = img.crop(crop)
    img.save(os.path.join(OUT, name + ".jpg"), quality=90, optimize=True)
    return img.size


if __name__ == "__main__":
    only = set(sys.argv[1:])
    for n, job in JOBS.items():
        if only and n not in only:
            continue
        print(n, build(n, *job))
