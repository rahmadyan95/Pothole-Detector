# import tkinter as tk
# from tkinter import ttk
import customtkinter as ctk
from customtkinter import*
# from tkinter import*
from tkinter import font
from ttkbootstrap import * 

class tkinterApp(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        container = ctk.CTkFrame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, Page1, Page2, Page3):
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
        
        custom_font = font.Font(family="Bahnschrift SemiBold SemiConden",size=100, weight="bold")

        side_bar = CTkCanvas(self, width=150,
                                    height=1100, 
                                    bg="gray10",
                                    highlightthickness=0,
                                    )
        side_bar.pack(side=tk.LEFT, fill=tk.Y)

        title = tk.Label(self,text = "POTHOLE",font = custom_font,fg="white",bg="gray20")
        title.place(x=200,y=50)

        title1 = tk.Label(self,text = "AUTODETECTOR",font = custom_font,fg="white",bg="gray20")
        title1.place(x=200,y=200)

        #Detection Button

        kamera_image = PhotoImage(file=r".\app_asset\kamera.png").subsample(3,3)
        page1_button = CTkButton(self, width=500, 
                          height=150, text='DETECT POTHOLE',
                          fg_color='grey', text_color='grey10',
                          command=lambda: controller.show_frame(Page1),
                          font=("Bahnschrift SemiBold SemiConden",45),
                          hover_color="#fce101",image=kamera_image,
                          
                          )
        page1_button.place(x=100,y=200)

        
        image_path1 = os.path.join(os.path.dirname(__file__), 'app_asset\maps.png')
        image1 = CTkImage(light_image=Image.open(image_path1), size=(90,90))
        page2 = CTkButton(self, width=500, 
                          height=150, text='  SHOW MAPS',
                          fg_color='grey', text_color='gray10',font=("Bahnschrift SemiBold SemiConden",45),
                          command=lambda: controller.show_frame(Page2),
                          hover_color="#fce101",
                          image=image1

                          )
        page2.place(x=100,y=360)

        
        # image_label1 = CTkLabel(page2,image=image1,text='',bg_color='grey20')
        # image_label1.place(x=1000)

        image_path2 = os.path.join(os.path.dirname(__file__), 'app_asset\document.png')
        image2 = CTkImage(light_image=Image.open(image_path2), size=(90,90))

        page3 = CTkButton(self, width=500, 
                          height=150, text=' SHOW DATA',
                          fg_color='grey', text_color='gray10',
                          command=lambda: controller.show_frame(Page3),
                          hover_color="#fce101",
                          image=image2,
                          font=("Bahnschrift SemiBold SemiConden",45)
                          
                          )
        page3.place(x=100,y=520)

        image_home = os.path.join(os.path.dirname(__file__), 'app_asset\home.png')
        imagehome = CTkImage(light_image=Image.open(image_home), size=(45,45))
        image_home = CTkLabel(self,image=imagehome,text='',bg_color='grey20',width=100, height=100)
        image_home.place(x=-12,y=45)
        

        side_background = Canvas(self, width=1250, height= 940, background="grey", highlightthickness=0)
        side_background.place(x=1250,y=400)

        title_side = CTkLabel(self,text="SYSTEM INFORMATION", font=("Bahnschrift SemiBold SemiConden",18),text_color="grey10",bg_color="grey")
        title_side.place(x=865, y=220)

        camera_logo_path = os.path.join(os.path.dirname(__file__), 'app_asset\map.png')
        imagehome = CTkImage(light_image=Image.open(camera_logo_path), size=(55,55))
        image_camera = CTkLabel(side_bar,image=imagehome,text='',bg_color='grey10',width=100, height=100)
        image_camera.place(x=-12,y=260)


        #============================= Untuk memasukan Foto ==================================================== #
        image_path = os.path.join(os.path.dirname(__file__), 'app_asset\construction.png')
        image = CTkImage(light_image=Image.open(image_path), size=(90,90))
        image_label = CTkLabel(self,image=image,text='',bg_color='grey20')
        image_label.place(x=375,y=20)
        #============================= Untuk memasukan Foto ==================================================== #


        title_side = CTkLabel(self,text="Beta Ver0.01.05", font=("Bahnschrift SemiBold SemiConden",12),text_color="grey",bg_color="grey20")
        title_side.place(x=1190, y=680)

        camera_logo_path = os.path.join(os.path.dirname(__file__), 'app_asset\kamera2.png')
        imagehome = CTkImage(light_image=Image.open(camera_logo_path), size=(45,45))
        image_camera = CTkLabel(side_bar,image=imagehome,text='',bg_color='grey10',width=100, height=100)
        image_camera.place(x=-12,y=150)

        camera_logo_path = os.path.join(os.path.dirname(__file__), 'app_asset\document1.png')
        imagehome = CTkImage(light_image=Image.open(camera_logo_path), size=(55,55))
        image_camera = CTkLabel(side_bar,image=imagehome,text='',bg_color='grey10',width=100, height=100)
        image_camera.place(x=-12,y=370)


class Page1(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        
        side_bar = CTkCanvas(self, width=150,
                                    height=1100, 
                                    bg="gray10",
                                    highlightthickness=0
                                    )
        side_bar.pack(side=tk.LEFT, fill=tk.Y)

        image_home = os.path.join(os.path.dirname(__file__), 'app_asset\home.png')
        imagehome = CTkImage(light_image=Image.open(image_home), size=(45,45))
        # image_home = CTkLabel(self,image=imagehome,text='',bg_color='grey10',height=100)
        # image_home.place(x=12,y=50)

        page3 = CTkButton(side_bar, 
                          text='',
                          fg_color='grey10',
                          command=lambda: controller.show_frame(StartPage),
                          hover_color="#fce101",
                          image=imagehome,
                          height=100,
                          width=75
                    
                          
                          )
        page3.place(x=0,y=45)

        camera_logo_path = os.path.join(os.path.dirname(__file__), 'app_asset\kamera2.png')
        imagehome = CTkImage(light_image=Image.open(camera_logo_path), size=(45,45))
        image_camera = CTkLabel(self,image=imagehome,text='',bg_color='grey20',width=100, height=100)
        image_camera.place(x=-12,y=150)

        camera_logo_path = os.path.join(os.path.dirname(__file__), 'app_asset\map.png')
        imagehome = CTkImage(light_image=Image.open(camera_logo_path), size=(55,55))
        image_camera = CTkLabel(side_bar,image=imagehome,text='',bg_color='grey10',width=100, height=100)
        image_camera.place(x=-12,y=260)

        camera_logo_path = os.path.join(os.path.dirname(__file__), 'app_asset\document1.png')
        imagehome = CTkImage(light_image=Image.open(camera_logo_path), size=(55,55))
        image_camera = CTkLabel(side_bar,image=imagehome,text='',bg_color='grey10',width=100, height=100)
        image_camera.place(x=-12,y=370)
        


class Page2(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        side_bar = CTkCanvas(self, width=150,
                                    height=1100, 
                                    bg="gray10",
                                    highlightthickness=0,
                                    )
        side_bar.pack(side=tk.LEFT, fill=tk.Y)

        image_home = os.path.join(os.path.dirname(__file__), 'app_asset\home.png')
        imagehome = CTkImage(light_image=Image.open(image_home), size=(45,45))
        # image_home = CTkLabel(self,image=imagehome,text='',bg_color='grey10',height=100)
        # image_home.place(x=12,y=50)

        page3 = CTkButton(side_bar, 
                          text='',
                          fg_color='grey10',
                          command=lambda: controller.show_frame(StartPage),
                          hover_color="#fce101",
                          image=imagehome,
                          height=100,
                          width=75
                    
                          
                          )
        page3.place(x=0,y=45)

        camera_logo_path = os.path.join(os.path.dirname(__file__), 'app_asset\kamera2.png')
        imagehome = CTkImage(light_image=Image.open(camera_logo_path), size=(45,45))
        image_camera = CTkLabel(side_bar,image=imagehome,text='',bg_color='grey10',width=100, height=100)
        image_camera.place(x=-12,y=150)

        camera_logo_path = os.path.join(os.path.dirname(__file__), 'app_asset\map.png')
        imagehome = CTkImage(light_image=Image.open(camera_logo_path), size=(55,55))
        image_camera = CTkLabel(side_bar,image=imagehome,text='',bg_color='grey20',width=100, height=100)
        image_camera.place(x=-12,y=260)

        camera_logo_path = os.path.join(os.path.dirname(__file__), 'app_asset\document1.png')
        imagehome = CTkImage(light_image=Image.open(camera_logo_path), size=(55,55))
        image_camera = CTkLabel(side_bar,image=imagehome,text='',bg_color='grey10',width=100, height=100)
        image_camera.place(x=-12,y=370)
        

class Page3(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        side_bar = CTkCanvas(self, width=150,
                                    height=1100, 
                                    bg="gray10",
                                    highlightthickness=0,
                                    )
        side_bar.pack(side=tk.LEFT, fill=tk.Y)

        image_home = os.path.join(os.path.dirname(__file__), 'app_asset\home.png')
        imagehome = CTkImage(light_image=Image.open(image_home), size=(45,45))
        # image_home = CTkLabel(self,image=imagehome,text='',bg_color='grey10',height=100)
        # image_home.place(x=12,y=50)

        page3 = CTkButton(side_bar, 
                          text='',
                          fg_color='grey10',
                          command=lambda: controller.show_frame(StartPage),
                          hover_color="#fce101",
                          image=imagehome,
                          height=100,
                          width=75
                    
                          
                          )
        page3.place(x=0,y=45)

        camera_logo_path = os.path.join(os.path.dirname(__file__), 'app_asset\kamera2.png')
        imagehome = CTkImage(light_image=Image.open(camera_logo_path), size=(45,45))
        image_camera = CTkLabel(side_bar,image=imagehome,text='',bg_color='grey10',width=100, height=100)
        image_camera.place(x=-12,y=150)

        camera_logo_path = os.path.join(os.path.dirname(__file__), 'app_asset\map.png')
        imagehome = CTkImage(light_image=Image.open(camera_logo_path), size=(55,55))
        image_camera = CTkLabel(side_bar,image=imagehome,text='',bg_color='grey10',width=100, height=100)
        image_camera.place(x=-12,y=260)

        camera_logo_path = os.path.join(os.path.dirname(__file__), 'app_asset\document1.png')
        imagehome = CTkImage(light_image=Image.open(camera_logo_path), size=(55,55))
        image_camera = CTkLabel(side_bar,image=imagehome,text='',bg_color='grey20',width=100, height=100)
        image_camera.place(x=-12,y=370)



if __name__ == "__main__":
    app = tkinterApp()
    app.title('Pothole Detector')
    app.geometry("1280x720")
    app.resizable(False,False)
    app.iconbitmap('app_asset/tool3_122846.ico')
    
    
    app.mainloop()

