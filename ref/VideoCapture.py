import cv2
import time
import numpy as np
import HandTrackingModule as htm

# ขนาดจอ
WIDTHCAM = 800
HIGHTCAM = 600

cap = cv2.VideoCapture(1)
cap.set(3, WIDTHCAM)
cap.set(4,HIGHTCAM)
previousTime = 0

imgBG = cv2.imread('image/bg.png')

# นำโมดูลมาใช้
detector = htm.handDetector()

while True:
    success, img = cap.read()
    
    img = detector.findHands(img)

    # ทำ FPS
    currentTime = time.time()
    fps = 1/(currentTime-previousTime)
    previousTime = currentTime

    # สร้าง text ขึ้นมาแสดงบนจอ
    cv2.putText(img, f'FPS: {int(fps)}', (40,50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)
    cv2.imshow("test", imgBG)
    cv2.imshow("Img", img)
    cv2.waitKey(1)
