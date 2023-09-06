import tkinter as tk
import detect
from tkinter import Button
from tkinter import filedialog

app = tk.Tk()
app.title("Pothole Detector")
app.geometry('800x400')

def start_detection():
    detect.detect()

start_button = Button(app, text="Start Detection", command=start_detection)
start_button.pack()


app.mainloop()


