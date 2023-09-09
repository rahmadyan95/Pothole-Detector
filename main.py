import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from customtkinter import*
from tkinter import*
from tkinter import font

class tkinterApp(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        container = ctk.CTkFrame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, Page1, Page2):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            

        self.show_frame(StartPage)
        

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        
        custom_font = font.Font(family="Norwester",size=90, weight="bold")

        side_background = CTkCanvas(self, width=150,
                                    height=1100, 
                                    bg="gray10",
                                    highlightthickness=0
                                    )
        side_background.pack(side=tk.LEFT, fill=tk.Y)

        title = tk.Label(self,
                        text = "POTHOLE\n  DETECTOR",
                        font = custom_font,
                        fg="white",
                        bg="gray20"
                        )
        title.pack(anchor=tk.NW, padx=40, pady=50)

        title = tk.Label(self,
                        text = "Powered By",
                        font = font.Font(family="Norwester",size=14, weight="bold"),
                        fg="white",
                        bg="gray20"
                        )
        title.pack(anchor=tk.NW, padx=40, pady=50)

        #Detection Button
        detect_button = CTkButton(self, width=220, 
                          height=300, text='',
                          fg_color='grey', text_color='black',
                          command=lambda: controller.show_frame(Page1)
                          )
        detect_button.pack(anchor=tk.NW, pady=20, padx=50, side=tk.LEFT)

        # Button untuk mengarahkan ke Page2
        page2_button = CTkButton(self, width=220,
                                height=300, text='',
                                fg_color='grey', text_color='black',
                                command=lambda: controller.show_frame(Page2)
                                )
        page2_button.pack(anchor=tk.NW, pady=20, padx=0, side=tk.LEFT)

        page3_button = CTkButton(self, width=220,
                                height=300, text='',
                                fg_color='grey', text_color='black',
                                command=lambda: controller.show_frame(Page2)
                                )
        page3_button.pack(anchor=tk.NW, pady=20, padx=50, side=tk.LEFT)


        

    

class Page1(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        
        side_background = CTkCanvas(self, width=150,
                                    height=1100, 
                                    bg="gray10",
                                    highlightthickness=0
                                    )
        side_background.pack(side=tk.LEFT, fill=tk.Y)

        label = ctk.CTkLabel(self, text="Ini adalah Page 1")
        label.pack()

class Page2(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        label = ctk.CTkLabel(self, text="Ini adalah Page 2")
        label.pack()


if __name__ == "__main__":
    app = tkinterApp()
    app.title('Pothole Detector')
    app.geometry('1100x600')
    app.mainloop()

