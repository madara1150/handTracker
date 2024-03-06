import os
import pickle
import cv2
import mediapipe as mp
import numpy as np
import Datacollection as create
import tool
import tkinter as tk

def run():
    window.destroy()
    model_dict = pickle.load(open('./model.p', 'rb'))
    model = model_dict['model']
    cap = cv2.VideoCapture(1)
    mp_hands = mp.solutions.hands
    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles

    hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

    labels_dict = tool.check_folders()
    while True:

        data_aux = []
        x_ = []
        y_ = []

        ret, frame = cap.read()
        if not ret:
            print("Error: Unable to capture frame from camera")
            break

        H, W, _ = frame.shape

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = hands.process(frame_rgb)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    frame,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())

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

            predicted_character = labels_dict[int(prediction[0])]

            # ทดสอบปิด
            # if labels_dict[int(prediction[0])] == "L":
            #     break

            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), 4)
            cv2.putText(frame, predicted_character, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 0, 0), 3,
                        cv2.LINE_AA)

        cv2.imshow('frame', frame)
        cv2.waitKey(1)
    cap.release()
    cv2.destroyAllWindows()

def create_map():
    window.destroy()
    create.main()

def create_gui():
    global window
    window = tk.Tk()
    window.title("FINGER FOCUS")
    window.resizable(True, True)

    window.geometry("700x800")

    # สร้าง frame หลักสำหรับจัดเรียงปุ่ม
    main_frame = tk.Frame(window)
    main_frame.pack(expand=True, fill="both")

    # ปรับแต่ง layout ของ frame หลัก
    main_frame.columnconfigure(0, weight=1)
    main_frame.columnconfigure(1, weight=1)
    main_frame.rowconfigure(0, weight=1)
    main_frame.rowconfigure(1, weight=1)

    # สร้างปุ่ม "START" และ "CREATE"
    run_button = tk.Button(main_frame, text="START", command=run, fg="black", bg="green")
    create_button = tk.Button(main_frame, text="CREATE", command=create_map, fg="black", bg="white")

    # วางปุ่ม "START" และ "CREATE" ใน frame หลัก
    run_button.grid(row=0, column=0, sticky="nsew")
    create_button.grid(row=1, column=0, sticky="nsew")

    window.mainloop()


create_gui()
