import os
import pickle
import cv2
from sklearn.ensemble import RandomForestClassifier
import mediapipe as mp
import numpy as np
import Datacollection as create
import tool
import tkinter as tk
import tkinter.font as tkFont
import time as tm
import threading
import time

def run(timeout):
    # รูป crop
    overlay_image = cv2.imread('crop/0/70.jpg')

    # ดึงค่าโมเดล
    model_dict = pickle.load(open('./model.p', 'rb'))
    model = model_dict['model']  

    cap = cv2.VideoCapture(1)

    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

    # อ่านโฟร์ดเดอร์แปลงเป็นด่าน JSON
    labels_dict = tool.check_folders()

    # ด่าน
    level = tool.get_fileCrop()
    level_currrent = 0
    print("level : ", level_currrent)

    # เวลา
    start_time = time.time() 
    duration = timeout

    #text
    text = ""
    time_text = ""

    while True:
        
        data_aux = []
        x_ = []
        y_ = []

        ret, frame = cap.read()
        if not ret:
            print("Error: ไม่พบกล้อง")
            break
        
        H, W, _ = frame.shape

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        cv2.putText(frame, str(level_currrent), (600,50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 0, 0), 3,
                        cv2.LINE_AA)
        
        results = hands.process(frame_rgb)

        # หามือเมื่อเจอมือ
        if results.multi_hand_landmarks:

            # สร้างจุดมาคให้กับมือ
            for hand_landmarks in results.multi_hand_landmarks:
                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y

                    x_.append(x)
                    y_.append(y)

                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y
                    data_aux.append(x - min(x_))
                    data_aux.append(y - min(y_))

            x1 = int(min(x_) * W) - 10
            y1 = int(min(y_) * H) - 10

            x2 = int(max(x_) * W) - 10
            y2 = int(max(y_) * H) - 10
            
            prediction = model.predict([np.asarray(data_aux)])

            # ตัวอักษรบอก level
            predicted_character = labels_dict[int(prediction[0])]

            # เช็คด่าน
            if labels_dict[int(prediction[0])] == str(level_currrent):
                text = "nice!!"
                time.sleep(1)
                
                # ไปเลเวลถัดไป
                if level_currrent + 1 < len(level):
                    level_currrent += 1
                    overlay_image = cv2.imread(f'crop/{level_currrent}/70.jpg')

                # เลเวลสุดท้าย
                else:
                    time_text = f'time : {timeout}s time played: {int(duration-time_left)}s'
                    print(f"เวลาที่เลือก :{duration} วินาที สถิตของคุณที่ทำได้คือ {int(duration-time_left)} วินาที")

            # put Text กับ box
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), 4)
            cv2.putText(frame, text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 0, 0), 3,
                        cv2.LINE_AA)
            text = ""
            cv2.imshow("overlay", overlay_image)

        # นับเวลาถ่อยหลัง
        time_left = duration - (time.time() - start_time)
        cv2.putText(frame, f"Time left: {int(time_left)}s", (900, 50), 
                cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 0), 2)
        cv2.putText(frame, time_text, (900, 100), 
                            cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 0), 2)

        cv2.imshow('frame', frame)

        if time_left <= 0:
            time_text = f'time played: time out!!'
            break

        cv2.waitKey(1)
    cap.release()
    cv2.destroyAllWindows()