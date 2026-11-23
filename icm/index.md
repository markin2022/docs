---
title: IP Camera 웹 설정 매뉴얼
description: MARKIN IP 카메라 웹 브라우저 설정(Web UI) 사용자 매뉴얼
---

# IP Camera 웹 설정 매뉴얼

> 이 문서는 웹 브라우저로 **MARKIN IP 카메라**에 접속해 **라이브 영상 확인 · 영상/카메라 화질 설정 · 네트워크 설정 · 모션/AI 이벤트 설정**을 하는 방법을 설명합니다.
>
> 화면은 영어(ENGLISH) UI 기준입니다.

## 목차
{: .no_toc}

* 목차
{:toc}

---

## 1. 시작하기

### 1.1 준비 사항

| 항목 | 내용 |
| --- | --- |
| PC 브라우저 | Chrome / Edge 최신 버전 권장 (별도 플러그인 설치 불필요) |
| 네트워크 | 카메라와 PC가 같은 네트워크(대역)에 연결되어 있어야 함 |
| 카메라 IP | 기본은 **DHCP**. IP를 모를 때는 [mInstaller](../mInstaller/)로 검색 |
| 기본 계정 | ID `admin` / 비밀번호는 설치 담당자에게 확인 (최초 로그인 후 변경 권장, 6.4 참고) |

> 💡 DHCP 서버가 없는 환경에서도 카메라는 **ZEROCONF IP**(`169.254.x.x`)를 함께 가집니다. PC를 같은 `169.254.x.x` 대역으로 설정하면 이 주소로도 접속할 수 있습니다.

### 1.2 접속 및 로그인

![로그인 화면](images/login.jpg)

1. 브라우저 주소창에 `http://<카메라 IP>/` 를 입력합니다. (예: `http://192.168.45.59/`)
2. **ID** 와 **PASSWORD** 를 입력합니다.
3. 로그인 후 처음 열 화면을 고릅니다.
   - **LIVE** : 라이브 영상 화면 (3장)
   - **SETUP** : 설정 화면 (5장)
4. **LOGIN** 버튼을 누릅니다.

> 화면 아래쪽에는 모델명 · 펌웨어 버전 · MAC 주소가 표시됩니다.

---

## 2. 화면 구성

모든 화면 위쪽에는 같은 도구 막대가 있습니다.

| 위치 | 버튼 | 기능 |
| --- | --- | --- |
| 왼쪽 위 | **로그아웃** (⇦ 모양) | 로그아웃하고 로그인 화면으로 이동 |
| 가운데 | **LIVE** (카메라 모양) | 라이브 영상 화면 (3장) |
| 가운데 | **Ai** | AI 라이브 화면 — 객체 박스·이벤트 확인 (4장) |
| 가운데 | **SETUP** (톱니바퀴) | 설정 화면 (5장 ~ 9장) |
| 오른쪽 위 (LIVE) | **SNAPSHOT** | 현재 영상을 이미지 파일로 저장 |
| 오른쪽 위 (LIVE) | **FULL SCREEN** | 영상을 전체 화면으로 보기 |
| 오른쪽 위 (SETUP) | 모델명 · 버전 | 현재 펌웨어 버전 표시 |

---

## 3. 라이브 화면 (LIVE)

![라이브 화면](images/live.jpg)

| 영역 | 설명 |
| --- | --- |
| **≡ (메뉴)** | 왼쪽 패널 숨기기 / 보이기 |
| **STREAM 선택** | 볼 스트림 선택 — `STREAM 1`(메인) / `STREAM 2`(서브) / `STREAM 3` |
| **영상 영역** | 왼쪽 위에 코덱 · 해상도 표시 (예: `H264 1920×1080`) |
| **EVENT** | 모션 등 이벤트가 발생하면 아이콘이 표시됨 |
| **SYSTEM INFORMATION** | 모델, 버전, 네트워크 방식(DHCP/STATIC), IP, 서브넷, 게이트웨이, DNS, MAC, ZEROCONF IP |
| **PTZ CONTROL** | 줌 / 포커스 조작 (아래 표) |

### 3.1 PTZ CONTROL (줌 / 포커스)

| 버튼 | 기능 |
| --- | --- |
| 🔍+ / 🔍− | 줌 인 / 줌 아웃 |
| **+** / **−** | 포커스 수동 조정 (가까이 / 멀리) |
| **AF** | 오토 포커스 한 번 실행 |
| **QUICK ZOOM** | 슬라이더로 원하는 줌 위치로 바로 이동 |

> 💡 줌을 바꾼 뒤 초점이 흐리면 **AF** 버튼을 누르세요. 설정 화면의 **ZOOM/FOCUS** (7.5)에서도 같은 조작을 할 수 있습니다.

---

## 4. AI 라이브 화면 (Ai)

![AI 라이브 화면](images/live_ai.jpg)

AI 객체 검출 결과를 영상 위에 겹쳐 보여 주는 화면입니다. AI 기능은 **SETUP › EVENT › AI** (9.2)에서 켜야 동작합니다.

| 영역 | 설명 |
| --- | --- |
| **OVERLAY ON VIDEO** | 영상 위에 표시할 정보 — `ROI`(감시 영역), `OBJECT BOX`(객체 박스), `OBJECT INFO`(객체 이름·신뢰도) |
| **FILTER:LABEL** | 표시할 객체 종류 — PERSON, CAR, MOTORCYCLE, BICYCLE, TRUCK, BUS |
| **FILTER:EVENT** | 오른쪽 이벤트 목록에 표시할 이벤트 — INTRUSION, APPEARANCE, DISAPPEARED, LOITERING, ENTRY, EXIT |
| **EVENT (오른쪽)** | 발생한 AI 이벤트 목록 |

---

## 5. 설정 화면 (SETUP) 사용법

설정 화면은 **왼쪽 메뉴**와 **오른쪽 설정 영역**으로 나뉩니다. 메뉴 그룹(`+ SYSTEM` 등)을 누르면 하위 메뉴가 펼쳐집니다.

| 메뉴 그룹 | 하위 메뉴 |
| --- | --- |
| **SYSTEM** | SYSTEM INFORMATION · SYSTEM MANAGEMENT · DATE & TIME · USER MANAGEMENT · LOG |
| **VIDEO** | VIDEO STREAM · VIDEO SETUP · CAMERA SETUP · PRIVACY SETUP · ZOOM/FOCUS · OSD |
| **NETWORK** | INTERFACE · PORT · UPNP · RTSP / ONVIF |
| **EVENT** | MOTION SETUP · AI |

공통 버튼

| 버튼 | 기능 |
| --- | --- |
| 💾 (저장, 오른쪽 아래) | 현재 페이지의 설정을 카메라에 저장. **저장하지 않고 다른 메뉴로 이동하면 변경 내용이 적용되지 않습니다.** |
| ↶ (되돌리기, 각 표 아래) | CAMERA SETUP 등에서 해당 표의 값을 기본값으로 되돌림 |

> ⚠️ CAMERA SETUP(7.3)에는 💾 저장 버튼이 없고, 슬라이더·콤보를 바꾸면 바로 카메라에 적용됩니다. 나머지 메뉴는 💾 저장을 눌러야 적용됩니다.

---

## 6. SYSTEM

### 6.1 SYSTEM INFORMATION

![SYSTEM INFORMATION](images/sys_info.jpg)

| 항목 | 설명 |
| --- | --- |
| MODEL / VERSION | 모델명, 펌웨어 버전, OpenSSL 버전 |
| LANGUAGE | 웹 화면 언어 — ENGLISH, KOREAN, JAPANESE, SIMPLIFIED CHINESE, TRADITIONAL CHINESE, GERMAN |
| NETWORK | 현재 IP 와 방식(DHCP/STATIC) |
| DATE & TIME | 카메라 현재 시각 |
| STATUS | 동작 시간(UP), CPU 사용률, 메모리(전체/사용/여유) |
| SERVICE PORTS | 현재 열려 있는 서비스 포트 목록 |
| **CONNECTION LIST** | 최근 영상 접속 기록 — 접속 IP, 스트림(MAIN/SUB), 프로토콜(RTSP 등), 접속 시각 |

### 6.2 SYSTEM MANAGEMENT

![SYSTEM MANAGEMENT](images/sys_manager.jpg)

| 항목 | 설명 |
| --- | --- |
| **SYSTEM REBOOT** (⏻) | 카메라 재시작 |
| **FACTORY DEFAULT** (↶) | 공장 초기화. **Keep Network Configuration** 을 체크하면 IP 등 네트워크 설정은 유지 |
| **FIRMWARE UPGRADE** (⤒) | 펌웨어 파일을 선택하면 업그레이드 시작. 아래에 현재 펌웨어 버전과 NPU(AI) 버전 표시 |
| **EXPORT** (⤓) | 체크한 항목의 설정을 파일로 저장 — ALL, DATE & TIME, USER MANAGEMENT, VIDEO, EVENT, CAMERA SETUP, DAY & NIGHT, NETWORK INTERFACE, NETWORK SERVICE, EVENT AI |
| **IMPORT** (⤒) | 저장해 둔 설정 파일을 불러와 적용 |

> ⚠️ 펌웨어 업그레이드 중에는 **전원을 끄거나 브라우저를 닫지 마세요.** 완료 후 카메라가 자동으로 재시작합니다.
>
> 💡 여러 대에 같은 설정을 넣을 때는 한 대를 설정한 뒤 **EXPORT** → 다른 카메라에서 **IMPORT** 하면 편리합니다. (네트워크 설정을 옮기지 않으려면 NETWORK INTERFACE 는 체크하지 마세요.)

### 6.3 DATE & TIME

![DATE & TIME](images/sys_date.jpg)

| 구역 | 항목 | 설명 |
| --- | --- | --- |
| DATE / TIME CONFIGURATION | CURRENT DATE / TIME, TIME ZONE | 현재 카메라 시각과 시간대 |
| **SET DATE / TIME** (체크해서 사용) | SYSTEM TIME | **USE CURRENT SYSTEM TIME** — 접속한 PC 시각으로 맞춤 |
| | NEW DATE / TIME | 날짜·시·분·초 직접 입력 |
| | TIME ZONE | 시간대 선택 (한국은 GMT+9 시간대) |
| | DAY LIGHT SAVING | 일광절약시간(DST) 사용 |
| DATE / TIME FORMAT | DATE FORMAT / TIME FORMAT | 영상 OSD 등에 표시되는 날짜·시간 형식 |
| TIME SYNC | TIME SYNC MODE | `NONE` 또는 `SERVER`(NTP 서버와 자동 동기화) |

### 6.4 USER MANAGEMENT

![USER MANAGEMENT](images/sys_user.jpg)

- **USER LIST** : 등록된 사용자 목록. **EDIT** 로 수정, **DELETE** 로 삭제, **NEW** 로 새 사용자 입력 시작
- **ADD / MODIFY** : 사용자 정보 입력 후 **ADD**(추가) 또는 **MODIFY**(수정)

| 항목 | 설명 |
| --- | --- |
| USER ID | 영문+숫자 5~16자 |
| DESCRIPTION | 사용자 설명 |
| PASSWORD / CONFIRM PASSWORD | 영문 소문자·대문자·숫자·특수문자 중 **3종류 이상 조합, 9자 이상**. 공백, 반복·연속 문자는 사용할 수 없음 |
| PERMISSION | `Live`(영상 보기) / `Setup`(설정 변경) 권한 |

> 💡 보안을 위해 설치 후 `admin` 비밀번호를 반드시 변경하고, 영상만 보는 사용자에게는 `Live` 권한만 주세요.

### 6.5 LOG

![LOG](images/sys_log.jpg)

카메라 동작 기록(RTSP 접속/종료, 스트림 설정 변경 등)을 시간 순서로 보여 줍니다.

- 오른쪽 위 콤보(예: `1/5`)로 페이지를 바꿉니다.
- **Log usage** 에 로그 저장 공간 사용량이 표시됩니다.
- **CLEAR** 를 누르면 로그를 모두 지웁니다.

---

## 7. VIDEO

### 7.1 VIDEO STREAM

![VIDEO STREAM](images/av_video_stream.jpg)

**VIDEO SOURCE › RESOLUTION** 에서 센서 출력 모드를 고릅니다 — `1920×1080 (30fps)` 또는 `1920×1080 (60fps)`.

**VIDEO CONFIGURATION** 에서 스트림 3개를 각각 설정합니다.

| 항목 | 설명 |
| --- | --- |
| STREAM | `#1` 메인 / `#2` 서브 / `#3` 세 번째 스트림 (RTSP 주소는 8.4 참고) |
| CODEC | `H.264` / `H.265` (#3은 `MJPEG`) |
| PROFILE | H.264 프로파일 — BASELINE / MAIN / HIGH |
| MODE | `VBR`(가변 비트레이트, 화질 우선) / `CBR`(고정 비트레이트, 대역폭 우선) |
| RESOLUTION | 640×360, 640×480, 800×600, 1280×720, 1920×1080 등 |
| FPS | 초당 프레임 수 (1 ~ 30, 60fps 모드에서는 최대 60) |
| QUALITY | VBR 화질 — LOW / STANDARD / HIGH / HIGHEST |
| MAX BITRATE | 최대 비트레이트 (32 Kbps ~ 수 Mbps) |
| GOP | I-프레임 간격 (보통 FPS와 같게 설정) |

> 💡 NVR 녹화용으로는 #1을 `H.265 / 1920×1080 / 30fps`, 모바일·다채널 보기용으로는 #2를 낮은 해상도로 쓰는 것을 권장합니다.

### 7.2 VIDEO SETUP

![VIDEO SETUP](images/av_video_setup.jpg)

| 항목 | 설명 |
| --- | --- |
| VIDEO SIGNAL | 아날로그(CVBS) 출력 방식 — `NTSC` / `PAL` |
| VIDEO FLIP | **VERTICAL FLIP**(상하 반전), **HORIZONTAL FLIP**(좌우 반전) |
| VIDEO ROTATION | 영상 회전 — `OFF` / `90degree` / `270degree`. 복도처럼 세로로 긴 장소를 찍을 때 사용(코리더 모드) |

> 영상 오른쪽 아래 ▦ 버튼을 누르면 미리보기 위에 격자를 표시해 화각·수평 맞추기를 도와줍니다.

### 7.3 CAMERA SETUP

![CAMERA SETUP](images/av_camera_setup.jpg)

위쪽 미리보기로 결과를 보면서 화질을 조정합니다. 값은 바꾸는 즉시 영상에 반영됩니다. 아래쪽 **CAMERA CONFIGURATION** 은 5개 탭으로 나뉩니다.

#### EXPOSURE (노출)

![EXPOSURE 탭](images/cam_exposure.jpg)

| 항목 | 설명 |
| --- | --- |
| BRIGHTNESS | 목표 밝기 |
| IRIS MODE | `ELC`(전자 셔터로 밝기 제어) / `ALC`(DC-IRIS 렌즈 조리개로 제어) |
| SHUTTER | `AUTO`(범위 안에서 자동) / `MANUAL`(고정) / `FLICKER`(형광등 깜빡임 방지). 오른쪽 콤보로 셔터 속도 범위 지정 (1/30 ~ 1/30000) |
| DSS | 저속 셔터 — `OFF` / `x2` / `x4`. 어두운 곳에서 밝아지지만 움직임 잔상이 생길 수 있음 |
| AGC | 최대 게인(증폭). 높을수록 어두운 곳이 밝지만 노이즈 증가 |
| ANTI-SATURATION | 밝은 부분 포화(번짐) 억제 |
| CONTROL SPEED | IRIS / SHUTTER / AGC 가 바뀌는 속도 |

#### COLOR (색상)

![COLOR 탭](images/cam_color.jpg)

| 항목 | 설명 |
| --- | --- |
| AWB MODE | 화이트밸런스 — `AUTO` / `AUTOext`(넓은 색온도 범위 자동) / `MANUAL`(R/G/B-GAIN 직접 조정) |
| R-GAIN / G-GAIN / B-GAIN | 수동 화이트밸런스 색 게인 |
| HUE & CHROMA | 색 영역별 색조(… TO …)와 채도(… CHROMA) 미세 조정 |

#### IMAGE (영상 개선 / 노이즈)

![IMAGE 탭](images/cam_image.jpg)

| 항목 | 설명 |
| --- | --- |
| SHARPNESS | 선명도 |
| CONTRAST | 대비 |
| GAMMA | 감마 값(0.40 ~ 0.75)과 방식(`LOW SAT.` / `TRADITIONAL`) |
| ACE | 어두운 부분 밝기 보정 — OFF / LOW / MIDDLE / HIGH |
| DEFOG | 안개·연무 보정 — OFF / LOW / MIDDLE / HIGH |
| 3DNR / NIGHT 3DNR | 시간축 노이즈 제거 (주간 / 야간) |
| 3DNR AGC SYNC. | 게인에 맞춰 3DNR 강도 자동 조절 |
| 2DNR / NIGHT 2DNR / 2DNR EDGE | 공간축 노이즈 제거 (주간 / 야간 / 경계 보존) |

#### WDR (광역 역광 보정)

![WDR 탭](images/cam_wdr.jpg)

| 항목 | 설명 |
| --- | --- |
| USE | WDR 사용 여부. 켜면 아래 항목이 활성화됨 |
| MODE | `ISP FRAME` / `LINE HDR` |
| LINE HDR MODE | `2PAGE` / `3PAGE` |
| WEIGHT | 보정 강도 — LOW / MIDDLE / HIGH |
| NIGHT(%) / BRIGHTNESS / CONTRAST | 야간 적용 비율, WDR 밝기·대비 |
| WDR GAMMA | WDR 사용 시 감마 |

> 💡 창문·출입구처럼 밝은 곳과 어두운 곳이 함께 보이는 장소에서 WDR 을 켜세요.

#### DAY & NIGHT (주야간 전환)

![DAY & NIGHT 탭](images/cam_daynight.jpg)

| 항목 | 설명 |
| --- | --- |
| MODE | `AUTO`(밝기에 따라 자동) / `DAY`(항상 컬러) / `NIGHT`(항상 흑백) / `EXT_ADC`·`EXT(LOW)`·`EXT(HIGH)`(외부 조도 센서 신호로 전환) / `SCHEDULE`(시간대 지정) |
| DELAY | 주야간 전환 지연 시간 (잦은 전환 방지) |
| IR LED | 적외선 LED — `AUTO`(야간에 자동 점등) / `ON` / `OFF` |

### 7.4 PRIVACY SETUP

![PRIVACY SETUP](images/av_privacy_setup.jpg)

영상의 일부를 가려(마스킹) 보이지 않게 합니다.

1. **USE PRIVACY** 를 체크합니다.
2. **ZONE** 에서 영역 번호(0 ~ 3, 최대 4개)를 고르고 **MASK** 를 체크합니다.
3. **COLOR** 에서 가림 색을 고릅니다 (WHITE, YELLOW, CYAN, GREEN, MAGENTA, RED, BLUE, BLACK).
4. **POSITION** 화살표로 위치를, **SIZE** 화살표로 크기를 조정합니다. **MOVE STEP**(40 ~ 400)은 버튼 한 번에 움직이는 양입니다.
5. 💾 저장합니다. **DEFAULT** 를 누르면 영역 위치·크기를 기본값으로 되돌립니다.

### 7.5 ZOOM/FOCUS

![ZOOM/FOCUS](images/sys_ptz.jpg)

| 항목 | 설명 |
| --- | --- |
| MODEL | 장착된 렌즈 모델 (예: `2M_AF2812Y`) |
| ZOOM | 줌 인 / 줌 아웃, **LENS INITIALIZATION**(렌즈 위치 초기화) |
| FOCUS | 포커스 + / −, **AUTO FOCUS**(오토 포커스 실행) |
| OPTIONS | **AF on Day/Night Switch** — 주야간 전환 시 자동으로 AF 실행 (IR 전환 후 초점 틀어짐 방지) |
| | **Use PTZ control lock** — 줌/포커스 조작 잠금 |

> 💡 설치 후 화각을 맞출 때: 줌으로 화각 조정 → **AUTO FOCUS** → 필요하면 FOCUS +/− 로 미세 조정.

### 7.6 OSD

![OSD](images/av_osd_setup.jpg)

영상 위에 제목과 날짜·시간 글자를 표시합니다.

| 항목 | 설명 |
| --- | --- |
| DISPLAY | 표시할 내용 — `OFF` / `TITLE` / `DATE TIME` / `TITLE+DATE TIME` |
| TITLE | 표시할 제목 글자와 색(WHITE / BLACK / RED / BLUE / GREEN) |
| DATE TIME | 날짜·시간 표시 색 (형식은 6.3 DATE / TIME FORMAT 을 따름) |
| FONT SIZE | 글자 크기 |

미리보기의 **주황 박스(제목)** 와 **파란 박스(날짜·시간)** 를 마우스로 끌어 표시 위치를 옮길 수 있습니다.

---

## 8. NETWORK

### 8.1 INTERFACE

![INTERFACE](images/net_interface.jpg)

| 항목 | 설명 |
| --- | --- |
| NETWORK TYPE | `DHCP`(자동 IP) / `STATIC`(고정 IP). STATIC 이면 아래 항목을 직접 입력 |
| IP ADDRESS / SUBNET MASK / GATEWAY / DNS | 네트워크 주소 |
| MAC ADDRESS | 카메라 고유 MAC 주소 (변경 불가) |
| NETWORK SPEED | 랜 속도 (예: `10/100Base-TX` 자동 협상) |
| ZEROCONF IP | 체크 시 `169.254.x.x` 링크 로컬 주소를 함께 사용 |

> ⚠️ IP 를 바꾸고 저장하면 접속이 끊깁니다. 새 IP 로 다시 접속하세요. IP 를 잊었으면 [mInstaller](../mInstaller/)로 검색합니다.

### 8.2 PORT

![PORT](images/net_port.jpg)

| 항목 | 기본값 | 설명 |
| --- | --- | --- |
| WEB PORT | 80 | 웹(HTTP) 접속 포트 |
| HTTPS PORT | 443 | 보안 웹(HTTPS) 접속 포트 |
| BASE PORT | 9010 | 전용 프로그램(NVR/VMS) 연동 포트 |
| RTSP PORT | 554 | RTSP 영상 포트 (RTSP / ONVIF 메뉴에서 변경) |
| DEVICE SEARCH PORT | 9010 | mInstaller 장치 검색 포트. **CHANGE DEVICE SEARCH PORT** 체크 후 변경 |
| DEFAULT PORT | — | **RETURN TO DEFAULT PORT SETTING** 체크 후 저장하면 모든 포트를 기본값으로 |

> 포트 왼쪽 체크박스를 해제하면 해당 서비스를 사용하지 않습니다.

### 8.3 UPNP

![UPNP](images/net_upnp.jpg)

| 항목 | 설명 |
| --- | --- |
| USAGE | **USE UPNP** — 윈도우 네트워크 탐색기에 카메라가 표시되도록 함 |
| FRIENDLY NAME | 탐색기에 표시될 이름 |

### 8.4 RTSP / ONVIF

![RTSP / ONVIF](images/net_rtsp_onvif.jpg)

**RTSP CONFIGURATION**

| 항목 | 설명 |
| --- | --- |
| USE RTSP(RTP/RTCP) | RTSP 스트리밍 사용 |
| RTSP SECURITY | **ACCESS CONTROL** 체크 시 RTSP 접속에 ID/비밀번호 필요 |
| RTSP PORT | 기본 554 |
| RTSP ADDRESS | 스트림별 주소 — `rtsp://<IP>:554/stream1` (#1), `stream2` (#2), `stream3` (#3) |
| MULTICAST | **USE** 체크 시 스트림별 멀티캐스트 주소(224.0.0.0 ~ 239.255.255.255)·포트(30000 ~ 65535) 사용 |

**ONVIF CONFIGURATION**

| 항목 | 설명 |
| --- | --- |
| USE | ONVIF 사용 (NVR/VMS 자동 등록) |
| ONVIF SECURITY | **ACCESS CONTROL** 체크 시 ONVIF 인증 사용 |
| PORT | ONVIF 포트 (웹 포트와 같음, 기본 80) |

> 💡 VLC 에서 보기: **미디어 › 네트워크 스트림 열기** 에 `rtsp://<IP>:554/stream1` 입력. ACCESS CONTROL 을 켰다면 `rtsp://<ID>:<비밀번호>@<IP>:554/stream1` 형식으로 입력합니다.

---

## 9. EVENT

### 9.1 MOTION SETUP

![MOTION SETUP](images/event_motion.jpg)

**MOTION AREA** — 영상을 격자로 나눠 모션을 감지할 영역을 지정합니다. 빨간 칸이 감지 영역입니다.

- 마우스를 **왼쪽 위 → 오른쪽 아래** 로 끌면 영역 **선택**
- 마우스를 **오른쪽 아래 → 왼쪽 위** 로 끌면 영역 **해제**

**MOTION CONFIGURATION**

| 항목 | 설명 |
| --- | --- |
| POST-ALARM | 모션이 멈춘 뒤 이벤트 상태를 유지하는 시간 (예: 5 SEC) |
| MOTION SENSITIVITY | 감도 (높을수록 작은 움직임도 감지) |

> 모션이 감지되면 라이브 화면 EVENT 패널(3장)에 표시되고, ONVIF 이벤트로 NVR 에 전달됩니다.

### 9.2 AI

AI(NPU) 기반 객체 검출과 영상 분석(침입·배회 등)을 설정합니다. 위쪽 미리보기에서 검출 결과와 ROI 를 확인할 수 있습니다.

#### OBJECT DETECTION (객체 검출)

![OBJECT DETECTION](images/event_ai_od.jpg)

| 항목 | 설명 |
| --- | --- |
| USE OBJECT DETECTION | 객체 검출 사용 |
| MODEL | AI 모델 — `OBJECTS`(사람·차량 등) / `FACE`(얼굴) |
| LABEL | 객체별 표시 색(COLOR), 검출 기준값(THRESHOLD, 높을수록 확실한 것만), 크기 범위(WIDTH / HEIGHT 최소~최대) |
| NPU SPEED | AI 처리 속도 (1 ~ 7) |
| USE OSD | 검출 결과를 영상에 직접 표시 — SHAPE(`BOX`/`MASK`), COLOR, MASK PATTERN, TRANSPARENCY |
| USE SNAPSHOT | AI 이벤트 스냅샷 기능 사용 |

> 💡 **USE OSD** 의 `MASK` 를 쓰면 검출된 사람·차량을 가려서 내보낼 수 있습니다 (개인정보 보호용).

#### VIDEO ANALYTICS (영상 분석)

![VIDEO ANALYTICS 미리보기](images/event_ai_va.jpg)

미리보기에 선택한 ROI(빨간 선)가 표시됩니다. 미리보기 아래 오른쪽 버튼(✏ 등)으로 ROI 를 새로 그리거나 수정합니다.

![VIDEO ANALYTICS 설정](images/event_ai_va_cfg.jpg)

| 항목 | 설명 |
| --- | --- |
| ROI | 설정할 영역 — `REGION #1~#4`(다각형 영역) / `LINE #1~#4`(통과선) |
| USE / LABEL | 영역 사용 여부와 이름 |
| OBJECT | 감시할 객체 — PERSON, CAR, MOTORCYCLE, BICYCLE, TRUCK, BUS |
| EVENT | `INTRUSION`(영역 침입), `APPEARANCE`(나타남), `DISAPPEARED`(사라짐), `LOITERING`(배회, TIME 이상 머무름). LINE 은 ENTRY / EXIT(통과 방향) |
| LINKUP | **TO MOTION DETECTION** — AI 이벤트를 모션 이벤트로도 전달 (모션만 지원하는 NVR 연동용), **ALARM OUT** — 알람 출력 연동(알람 출력 단자가 있는 경우) |

---

## 10. 문제 해결

| 증상 | 확인 사항 |
| --- | --- |
| 웹 접속이 안 됨 | PC 와 카메라가 같은 대역인지 확인. [mInstaller](../mInstaller/)로 IP 를 검색하거나 ZEROCONF IP(`169.254.x.x`)로 접속 |
| 로그인이 안 됨 | ID/비밀번호 확인. 계속 실패하면 공장 초기화가 필요할 수 있음 (설치 업체 문의) |
| 영상이 안 나옴 | 다른 STREAM 선택, 브라우저 새로고침. VIDEO STREAM(7.1)의 코덱·해상도 확인 |
| 초점이 흐림 | ZOOM/FOCUS(7.5)에서 **AUTO FOCUS**. 주야간 전환 후 흐려지면 **AF on Day/Night Switch** 사용 |
| 밤에 영상이 너무 어둡거나 노이즈가 많음 | DAY & NIGHT(7.3) MODE·IR LED 확인, EXPOSURE 의 AGC·DSS, IMAGE 의 NIGHT 3DNR 조정 |
| NVR 에 등록이 안 됨 | RTSP / ONVIF(8.4)에서 ONVIF **USE** 확인, ACCESS CONTROL 사용 시 NVR 에 같은 계정 입력 |
| 설정을 바꿨는데 적용이 안 됨 | 페이지 오른쪽 아래 💾 저장을 눌렀는지 확인 |

---

<sub>영상 예시 이미지: “Teheran-ro Yeongdong-daero crossing 2” by kallerna, [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/), via [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Teheran-ro_Yeongdong-daero_crossing_2.jpg). 매뉴얼 스크린샷의 영상 영역에 합성되었습니다.</sub>
