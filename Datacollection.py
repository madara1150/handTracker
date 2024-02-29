import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math
import CheckImage as imgs
import os
import create_dataset as dataset

def main():
    cap = cv2.VideoCapture(0)
    counter = 0
    floder_check = 0

    # สร้างโฟร์ดเดอร์ที่ไม่มี
    while True:
        # ตรวจสอบว่าโฟลเดอร์มีอยู่หรือไม่
            if not os.path.exists(f"data/{floder_check}"):
                imgs.create_floder(floder_check)
                break
            else:
                floder_check += 1
    folder = f'data/{floder_check}/'
    while True:
        success, img = cap.read(1)
        cv2.imshow('Image', img)
        key = cv2.waitKey(1)
        if key == ord("s"):
            counter += 1
            cv2.imwrite(f'{folder}/{counter}.jpg', img)
            print(counter)
        if key == ord("q"):
            dataset.main() 
            break