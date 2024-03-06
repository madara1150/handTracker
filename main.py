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

        GButton_999=tk.Button(root)
        GButton_999["bg"] = "#067a16"
        ft = tkFont.Font(family='Times',size=28)
        GButton_999["font"] = ft
        GButton_999["fg"] = "#ffffff"
        GButton_999["justify"] = "center"
        GButton_999["text"] = "START"
        GButton_999.place(x=250,y=340,width=167,height=61)
        GButton_999["command"] = self.started

        GButton_748=tk.Button(root)
        GButton_748["bg"] = "#a29d9d"
        ft = tkFont.Font(family='Times',size=28)
        GButton_748["font"] = ft
        GButton_748["fg"] = "#ffffff"
        GButton_748["justify"] = "center"
        GButton_748["text"] = "CREATE"
        GButton_748.place(x=250,y=440,width=166,height=57)
        GButton_748["command"] = self.create

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

