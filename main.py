import tkinter as tk
import customtkinter as ctk
from customtkinter import*
from tkinter import font

window = ctk.CTk()
window.title('Pothole Detector')
window.geometry('1100x600')

custom_font = font.Font(family="Norwester",size=90, weight="bold")

side_background = CTkCanvas(window, width=150,
                            height=1100, 
                            bg="gray20",
                            highlightthickness=0
                            )
side_background.pack(side=tk.LEFT, fill=tk.Y)

title = tk.Label(window,
                 text = "POTHOLE\n  DETECTOR",
                 font = custom_font,
                 fg="white",
                 bg=window.cget("bg")
                 )
title.pack(anchor=tk.NW, padx=50, pady=50)

detect_button = CTkButton(window, width= 100, 
                          height= 100, text='',
                          fg_color='grey', text_color='black'
                          )
detect_button.pack(anchor=tk.SW, pady=20, padx= 30)




window.mainloop()

