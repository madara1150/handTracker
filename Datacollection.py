import cv2
from handDetector import HandDetector
import numpy as np
import math
import tool
import os
import create_dataset as dataset

def main():
    cap = cv2.VideoCapture(1)
    detector = HandDetector(maxHands=1)

    # constant
    counter = 0
    floder_check = 0
    folder_crop_check = 0
    offset = 20

    #text
    text = "Press S to save"
    counter_text = f'picture :{counter}/71'
    error_text = ""

    # สร้างโฟร์ดเดอร์ที่ไม่มี Data
    while True:
        # ตรวจสอบว่าโฟลเดอร์มีอยู่หรือไม่
            if not os.path.exists(f"data/{floder_check}"):
                tool.create_floder(floder_check)
                break
            else:
                floder_check += 1

    # สร้างโฟร์ดเดอร์ที่ไม่มี Image Crop
    while True:
        # ตรวจสอบว่าโฟลเดอร์มีอยู่หรือไม่
            if not os.path.exists(f"crop/{folder_crop_check}"):
                tool.create_floder_crop(folder_crop_check)
                break
            else:
                folder_crop_check += 1

    # path
    folder = f'data/{floder_check}/'
    folder_crop = f'crop/{folder_crop_check}/'

    while True:

        success, img = cap.read(1)
        hands, img = detector.findHands(img)

        # text แสดงบนหน้าจอ
        cv2.putText(img,text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 0, 0), 3,
                        cv2.LINE_AA)
        cv2.putText(img,counter_text, (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 0, 0), 3,
                        cv2.LINE_AA)
        cv2.putText(img,error_text, (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 0, 0), 3,
                        cv2.LINE_AA)
        
        cv2.imshow('Image', img)
        key = cv2.waitKey(1)

        # save รูป
        if key == ord("s") and counter <= 70:
            
            # ตรวจสอบมือ ตอน บันทึกภาพ
            if hands:
                counter += 1
                cv2.imwrite(f'{folder}/{counter}.jpg', img)
                print(f'จำนวนรูป : {counter} ที่เก็บ : {folder}')
                counter_text = f'picture :{counter}/71'
                error_text = ""
            else:
                error_text = "no hand pls again"

            # ให้บันทึกรุปแค่ 70 ภาพ
            if counter == 70:
                # ตรวจสอบรูป
                if hands:
                    hand = hands[0]
                    x, y, w, h = hand['bbox']
                    imgCrop = img[y-offset -50 :y + h + offset+50 , x-offset-50 :x + w + offset+50]
                    cv2.imwrite(f'{folder_crop}/{counter}.jpg', imgCrop)
                    print(folder_crop)
                    text = "Please Press Q"
                elif counter == 71:
                    error_text = "success!"
                else:

                    # เมื่อไม่พบมือจะทำการลบ model ออก
                    files = os.listdir(folder)
                    files_crop = os.listdir(folder_crop)
                    
                    # ลบไฟล์ใน data ทั้งหมด
                    for file in files:
                        os.remove(os.path.join(folder, file))
                    os.rmdir(folder)
                    
                    # ลบไฟล์ใน crop ทั้งหมด
                    for fileCrop in files_crop:
                        os.remove(os.path.join(folder_crop, fileCrop))
                    os.rmdir(folder_crop)

                    print("ไม่พบมือ")
                    break
        
        # ปิดโปรแกรม
        if key == ord("q"):
            dataset.main()
            break
