import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math
import tool
import os
import create_dataset as dataset

def main():
    cap = cv2.VideoCapture(1)
    counter = 0
    floder_check = 0

    # สร้างโฟร์ดเดอร์ที่ไม่มี
    while True:
        # ตรวจสอบว่าโฟลเดอร์มีอยู่หรือไม่
            if not os.path.exists(f"data/{floder_check}"):
                tool.create_floder(floder_check)
                break
            else:
                floder_check += 1
    folder = f'data/{floder_check}/'
    text = "Press S to save"
    while True:
        success, img = cap.read(1)
        cv2.putText(img,text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 0, 0), 3,
                        cv2.LINE_AA)
        cv2.imshow('Image', img)
        key = cv2.waitKey(1)
        if key == ord("s") and counter <= 70:
            counter += 1
            cv2.imwrite(f'{folder}/{counter}.jpg', img)
            print(counter)
            if counter == 70:
                 text = "Please Press Q"
        if key == ord("q"):
            dataset.main()
            break