import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import numpy as np
import math
from random import randrange
import time
import tool as imgs

offset = 20
imgSize = 300
counter = 0
previousTime = 0

# เปิดกล้อง
cap = cv2.VideoCapture(0)
# ตรวจจับมือ
detector = HandDetector(maxHands=1)
classifier = Classifier("Model/keras_model.h5" , "Model/labels.txt")

labels = ["Hello","I love you","No","Okay","Please","Thank you","Yes"]
all_img = imgs.get_filenames()

while True:
    success, img = cap.read()
    imgOutput = img.copy()
    hands, img = detector.findHands(img)

    # FPS
    currentTime = time.time()
    fps = 1/(currentTime-previousTime)
    previousTime = currentTime

    # ถ้าเจอมือ
    if hands:
        hand = hands[0]
        x, y, w, h = hand['bbox']

        imgWhite = np.ones((imgSize, imgSize, 3), np.uint8)*255
        
        # crop รูป
        imgCrop = img[y-offset:y + h + offset + 100, x-offset:x + w  + offset]
        imgCropSave = img[y-offset - 20:y + h + offset+ 20, x-offset-20:x + w  + offset+20]
        
        imgCropShape = imgCrop.shape

        # กด K เพื่อสร้างด่าน
        key = cv2.waitKey(1) & 0xFF
        if key == ord('k'):
            filename = "image/cropped_image_{}.jpg".format(randrange(50))
            filename2 = "image/full_image_{}.jpg".format(randrange(50))
            cv2.imwrite(filename, imgCropSave)
            cv2.imwrite(filename2, img)
            print("Image saved as:", filename)

        aspectRatio = h / w
        if not imgCrop.size:  # เช็ครูปว่าง
            print("Error ======> หารูปไม่เจอหรือ resize ไม่ได้")
        else: 
            if aspectRatio > 1:
                k = imgSize / h
                wCal = math.ceil(k * w)
                imgResize = cv2.resize(imgCrop, (wCal, imgSize))
                imgResizeShape = imgResize.shape
                wGap = math.ceil((imgSize-wCal)/2)
                imgWhite[:, wGap: wCal + wGap] = imgResize
                prediction , index = classifier.getPrediction(imgWhite, draw= False)
                print(prediction, index)

            else:
                k = imgSize / w
                hCal = math.ceil(k * h)
                imgResize = cv2.resize(imgCrop, (imgSize, hCal))
                imgResizeShape = imgResize.shape
                hGap = math.ceil((imgSize - hCal) / 2)
                imgWhite[hGap: hCal + hGap, :] = imgResize
                prediction , index = classifier.getPrediction(imgWhite, draw= False)

        

    # สร้าง text ขึ้นมาแสดงบนจอ
        # cv2.rectangle(imgOutput,(x-offset,y-offset-70),(x -offset+400, y - offset+60-50),(0,255,0),cv2.FILLED)  
        cv2.putText(imgOutput,labels[index],(x,y-30),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,0),2)
        if labels[index] == "Thank you":
            print("true ==================================")
        cv2.rectangle(imgOutput,(x-offset,y-offset),(x + w + offset, y+h + offset),(0,255,0),4)   
        
        # cv2.imshow('ImageCrop', imgCrop)
        # cv2.imshow('ImageWhite', imgWhite)

    # แสดง FPS
    cv2.putText(imgOutput, f'FPS: {int(fps)}', (40,50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)
    # แสดงหน้าจอ
    cv2.imshow('Image', imgOutput)
    cv2.waitKey(1)
    