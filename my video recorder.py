import cv2
import numpy as np

video_file = 'rtsp://210.99.70.120:1935/live/cctv005.stream'

cap = cv2.VideoCapture(video_file)

# 코덱 정의
fourcc = cv2.VideoWriter_fourcc(*'DIVX')

# 녹화 on / off
record = False

# 녹화 확인 용 원
COLOR =(0, 0, 255) # BGR 빨간색
RADIUS = 10 # 반지름

# 프레임 크기, FPS
width = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)
wait_msec = int(1 / fps * 1000)

out = cv2.VideoWriter('output.avi', fourcc, fps, (width, height))
#저장 파일명, 코덱, FPS, 크기 (width, height)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    if record:
        out.write(frame) # 영상 데이터만 저장 (소리 X)
        cv2.circle(frame, (20, 20), RADIUS, COLOR, cv2.FILLED, cv2.LINE_AA) # 꽉 찬 원
        
    cv2.imshow('video player',frame)

    key = cv2.waitKey(wait_msec)
    
    if key == 27: # ESC
        break

    if key == ord(' ') :
            record = True if record is False else False
        
out.release() # 자원 해제
cap.release()
cv2.destroyAllWindows()
