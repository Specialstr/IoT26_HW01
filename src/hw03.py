# 필요한 라이브러리 불러오기
from gpiozero import Button, MotionSensor  # GPIO 버튼, PIR 모션 센서 제어
from picamera2 import Picamera2            # 카메라 모듈 제어 (picamera2 버전)
from datetime import datetime              # 파일명에 날짜/시간 사용
import time                                # 딜레이 처리

# GPIO 핀 설정
button = Button(2)        # 버튼: GPIO 2번 핀 (카메라 정지용)
pir = MotionSensor(17)    # PIR 모션 센서: GPIO 17번 핀

# 카메라 초기화 및 시작
camera = Picamera2()
camera.start()
time.sleep(2)  # 카메라 안정화를 위해 2초 대기

# 사진 촬영 횟수 카운터
i = 0

# 버튼을 누르면 카메라를 정지하고 프로그램 종료
def stop_camera():
    camera.stop()  # 카메라 정지
    exit()         # 프로그램 종료

# 모션이 감지되면 사진을 촬영하는 함수
def take_photo():
    global i
    i += 1  # 촬영 횟수 증가
    
    # 현재 시간을 파일명에 포함 (예: motion_20260509_222127.jpg)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f'/home/pi/hw3/motion_{timestamp}.jpg'
    
    # 사진 촬영 및 저장
    camera.capture_file(filename)
    print(f'사진 찍음: {filename}')
    
    time.sleep(3)  # 연속 촬영 방지를 위해 3초 대기

# 이벤트 핸들러 등록
button.when_pressed = stop_camera  # 버튼 누르면 stop_camera 실행
pir.when_motion = take_photo       # 모션 감지되면 take_photo 실행

print("모션 감지 대기 중...")

# 프로그램이 종료되지 않고 계속 대기 (이벤트 발생까지)
from signal import pause
pause()
