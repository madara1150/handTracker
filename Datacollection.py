import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math
import CheckImage as imgs
import os

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)
offset = 20
imgSize = 300

counter = 0
floder_check = 0

# สร้างโฟร์ดเดอร์ที่ไม่มี
while True:
    # ตรวจสอบว่าโฟลเดอร์มีอยู่หรือไม่
        if not os.path.exists(f"img/{floder_check}"):
            imgs.create_floder(floder_check)
            break
        else:
            floder_check += 1
folder = f'img/{floder_check}/'

while True:
    success, img = cap.read(1)
    # hands, img = detector.findHands(img)
    # if hands:
    #     hand = hands[0]
    #     x, y, w, h = hand['bbox']

    #     imgWhite = np.ones((imgSize, imgSize, 3), np.uint8)*255

    #     imgCrop = img[y-offset:y + h + offset, x-offset:x + w + offset]
    #     imgCropShape = imgCrop.shape

    #     aspectRatio = h / w

    #     if aspectRatio > 1:
    #         k = imgSize / h
    #         wCal = math.ceil(k * w)
    #         imgResize = cv2.resize(imgCrop, (wCal, imgSize))
    #         imgResizeShape = imgResize.shape
    #         wGap = math.ceil((imgSize-wCal)/2)
    #         imgWhite[:, wGap: wCal + wGap] = imgResize

    #     else:
    #         k = imgSize / w
    #         hCal = math.ceil(k * h)
    #         imgResize = cv2.resize(imgCrop, (imgSize, hCal))
    #         imgResizeShape = imgResize.shape
    #         hGap = math.ceil((imgSize - hCal) / 2)
    #         imgWhite[hGap: hCal + hGap, :] = imgResize

    #     cv2.imshow('ImageCrop', imgCrop)
    #     cv2.imshow('ImageWhite', imgWhite)

    cv2.imshow('Image', img)
    key = cv2.waitKey(1)
    if key == ord("s"):
        counter += 1
        cv2.imwrite(f'{folder}/{counter}.jpg', img)
        print(counter)