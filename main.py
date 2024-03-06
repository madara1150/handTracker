import mediapipe as mp
import numpy as np
import Datacollection as create
import tkinter as tk
import tkinter.font as tkFont
import start

class App:
    def __init__(self, root):
        root.title("FINGER FUCUS")
        root.geometry("700x800")
        GLabel_318=tk.Label(root)
        GLabel_318["activebackground"] = "#b41a1a"
        ft = tkFont.Font(family='Times',size=48)
        GLabel_318["font"] = ft
        GLabel_318["fg"] = "#c71585"
        GLabel_318["justify"] = "center"
        GLabel_318["text"] = "FINGER FOCUS"
        GLabel_318.place(x=160,y=60,width=365,height=161)

        start_btn=tk.Button(root)
        start_btn["bg"] = "#067a16"
        ft = tkFont.Font(family='Times',size=28)
        start_btn["font"] = ft
        start_btn["fg"] = "#ffffff"
        start_btn["justify"] = "center"
        start_btn["text"] = "START"
        start_btn.place(x=250,y=340,width=167,height=61)
        start_btn["command"] = self.started

        create_btn=tk.Button(root)
        create_btn["bg"] = "#a29d9d"
        ft = tkFont.Font(family='Times',size=28)
        create_btn["font"] = ft
        create_btn["fg"] = "#ffffff"
        create_btn["justify"] = "center"
        create_btn["text"] = "CREATE"
        create_btn.place(x=250,y=440,width=166,height=57)
        create_btn["command"] = self.create

    def started(self):
        root.destroy()
        start.run()


    def create(self):
        root.destroy()
        create.main()

if __name__ == "__main__":
    global root
    root = tk.Tk()
    app = App(root)
    root.mainloop()

