# import tkinter as tk
# from tkinter import ttk
import socket
import customtkinter as ctk
from customtkinter import*
# from tkinter import*
from tkinter import font
from ttkbootstrap import * 
import cv2
from PIL import Image, ImageTk
import pandas as pd
from ultralytics import YOLO
from tracker import*
import cvzone
import curr_loc as curr_loc
import os
import datetime
from customtkinter import filedialog, BooleanVar
from CTkMessagebox import CTkMessagebox
from datetime import timedelta 
from datetime import timedelta
import ttkbootstrap as ttk
import psutil
import GPUtil
import tkintermapview as tkmap
import textwrap

class tkinterApp(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._set_appearance_mode("dark")
        
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
        
        background = CTkLabel(self,width=1280,height=720,text='',bg_color="grey20")
        background.place(x=0,y=0)

        self.updating_meter = False
        custom_font = font.Font(family="Bahnschrift SemiBold SemiConden",size=100, weight="bold")

        side_bar = CTkCanvas(background, width=150,
                                    height=1490, 
                                    bg="gray10",
                                    highlightthickness=0,
                                    )
        side_bar.place(x=0,y=0)

        title = tk.Label(background,text = "POTHOLE",font = custom_font,fg="white",bg="gray20")
        title.place(x=200,y=50)

        title1 = tk.Label(background,text = "AUTODETECTOR",font = custom_font,fg="white",bg="gray20")
        title1.place(x=200,y=200)

        #Detection Button

        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        kamera_image = CTkImage(light_image=Image.open(os.path.join(self.script_dir, 'app_asset', 'kamera.png')),size=(80,80))
        page1_button = CTkButton(background, width=500, 
                          height=150, text='DETECT POTHOLE',
                          fg_color='grey', text_color='grey10',
                          command=lambda: controller.show_frame(Page1),
                          font=("Bahnschrift SemiBold SemiConden",45),
                          hover_color="#fce101",image=kamera_image,bg_color='grey20'
                          
                          )
        page1_button.place(x=100,y=200)

        
        image_path1 = os.path.join(self.script_dir, 'app_asset', 'maps.png')
        image1 = CTkImage(light_image=Image.open(image_path1), size=(90,90))
        page2 = CTkButton(background, width=500, 
                          height=150, text='  SHOW MAPS',
                          fg_color='grey', text_color='gray10',font=("Bahnschrift SemiBold SemiConden",45),
                          command=lambda: controller.show_frame(Page2),
                          hover_color="#fce101",
                          image=image1,bg_color='grey20'

                          )
        page2.place(x=100,y=360)

        
        # image_label1 = CTkLabel(page2,image=image1,text='',bg_color='grey20')
        # image_label1.place(x=1000)

        image_path2 = image_path1 = os.path.join(self.script_dir, 'app_asset', 'document.png')
        image2 = CTkImage(light_image=Image.open(image_path2), size=(90,90))

        page3 = CTkButton(background, width=500, 
                          height=150, text=' SHOW DATA',
                          fg_color='grey', text_color='gray10',
                          command=lambda: controller.show_frame(Page3),
                          hover_color="#fce101",
                          image=image2,
                          font=("Bahnschrift SemiBold SemiConden",45),
                          bg_color='grey20'
                          
                          )
        page3.place(x=100,y=520)

        image_home = os.path.join(self.script_dir, 'app_asset', 'home.png')
        imagehome = CTkImage(light_image=Image.open(image_home), size=(45,45))
        image_home = CTkLabel(background,image=imagehome,text='',bg_color='grey20',width=100, height=100)
        image_home.place(x=-12,y=45)
        
        # RIGHT SIDE BOX ======================================================================================
        side_background = CTkButton(background, width=640, height= 468, bg_color="grey20",corner_radius=8, text='',state="disabled",fg_color="grey")
        side_background.place(x=620,y=200)

        title_side = CTkLabel(background,text="SYSTEM INFORMATION", font=("Bahnschrift SemiBold SemiConden",18),text_color="grey10",bg_color="grey")
        title_side.place(x=865, y=220)

        # RAM Status ===========================================================================================
        self.ram_status = CTkLabel(side_background,width=150,height=200,bg_color="grey30",text='')
        self.ram_status.place(x=20,y=60)

        self.ram_status_title = CTkLabel(self.ram_status,bg_color="grey30",text='RAM Usage', font=("Bahnschrift SemiBold SemiConden",18))
        self.ram_status_title.place(x=36,y=5)

        self.ram_number = CTkLabel(self.ram_status,width=130,height=150,bg_color="grey10",text='',text_color="white",
                                   font=("Bahnschrift SemiBold SemiConden",35))
        self.ram_number.place(x=10,y=40)


        # GPU STATUS ===============================================================================================

        self.GPU_status = CTkLabel(side_background,width=440,height=200,bg_color="grey30",text='')
        self.GPU_status.place(x=180,y=60)

        self.GPU_status_title = CTkLabel(self.GPU_status,bg_color="grey30",text='Graphical Processing Unit Information', font=("Bahnschrift SemiBold SemiConden",18))
        self.GPU_status_title.place(x=85,y=5)

        self.GPU_device_name = CTkLabel(self.GPU_status,width=230,height=45,bg_color="grey10",text='GPU Name',text_color="white",
                                   font=("Bahnschrift SemiBold SemiConden",18))
        self.GPU_device_name.place(x=10,y=40)

        self.gpu_name = CTkLabel(self.GPU_status,width=230,height=95,bg_color="grey10",text='',text_color="white",
                                   font=("Bahnschrift SemiBold SemiConden",14))
        self.gpu_name.place(x=10,y=90)

        # GPU NAME 
        self.GPU_load = CTkLabel(self.GPU_status,width=90,height=45,bg_color="grey10",text='GPU Load',text_color="white",
                                   font=("Bahnschrift SemiBold SemiConden",16))
        self.GPU_load.place(x=245,y=40)

        self.GpuLoadName = CTkLabel(self.GPU_status,width=90,height=95,bg_color="grey10",text='',text_color="white",
                                   font=("Bahnschrift SemiBold SemiConden",35))
        self.GpuLoadName.place(x=245,y=90)

        # GPU 
        self.GPU_Vram = CTkLabel(self.GPU_status,width=90,height=45,bg_color="grey10",text='VRAM Usage',text_color="white",
                                   font=("Bahnschrift SemiBold SemiConden",14))
        self.GPU_Vram.place(x=340,y=40)

        self.GPUVRAMNAME = CTkLabel(self.GPU_status,width=90,height=95,bg_color="grey10",text='',text_color="white",
                                   font=("Bahnschrift SemiBold SemiConden",35))
        self.GPUVRAMNAME.place(x=340,y=90)



        



        #============================= Untuk memasukan Foto ==================================================== #
        camera_logo_path = os.path.join(self.script_dir, 'app_asset', 'map.png')
        imagehome = CTkImage(light_image=Image.open(camera_logo_path), size=(55,55))
        image_camera = CTkLabel(side_bar,image=imagehome,text='',bg_color='grey10',width=100, height=100)
        image_camera.place(x=-12,y=260)

        image_path = os.path.join(self.script_dir, 'app_asset', 'construction.png')
        image = CTkImage(light_image=Image.open(image_path), size=(90,90))
        image_label = CTkLabel(self,image=image,text='',bg_color='grey20')
        image_label.place(x=375,y=20)
        #============================= Untuk memasukan Foto ==================================================== #


        title_side = CTkLabel(self,text="Beta Ver0.01.05", font=("Bahnschrift SemiBold SemiConden",12),text_color="grey",bg_color="grey20")
        title_side.place(x=1190, y=680)

        camera_logo_path = os.path.join(self.script_dir, 'app_asset', 'kamera2.png')
        imagehome = CTkImage(light_image=Image.open(camera_logo_path), size=(45,45))
        image_camera = CTkLabel(side_bar,image=imagehome,text='',bg_color='grey10',width=100, height=100)
        image_camera.place(x=-12,y=150)

        camera_logo_path = os.path.join(self.script_dir, 'app_asset', 'document1.png')
        imagehome = CTkImage(light_image=Image.open(camera_logo_path), size=(55,55))
        image_camera = CTkLabel(side_bar,image=imagehome,text='',bg_color='grey10',width=100, height=100)
        image_camera.place(x=-12,y=370)

        # self.update_meter()



        # OUTDORR STATUS =====================================
        

        main_outdoor_box = CTkLabel(side_background,height=180, width=600,bg_color="grey30", text='')
        main_outdoor_box.place(x=20, y=270)
        self.outdoor_title = CTkLabel(main_outdoor_box,bg_color="grey30",text='Enviroment Status', font=("Bahnschrift SemiBold SemiConden",18))
        self.outdoor_title.place(x=230,y=6)

        # Weather
        self.weather = CTkLabel(main_outdoor_box,width=130,height=40,bg_color="grey10",text='Temperature',text_color="white",
                                   font=("Bahnschrift SemiBold SemiConden",16))
        self.weather.place(x=20,y=40)

        self.weather_value = CTkLabel(main_outdoor_box,width=130,height=80,bg_color="grey10",text='',text_color="white",
                                   font=("Bahnschrift SemiBold SemiConden",35))
        self.weather_value.place(x=20,y=85)

        # Latitdue BOX
        self.latitude_box = CTkLabel(main_outdoor_box,width=130,height=40,bg_color="grey10",text='Latitude',text_color="white",
                                   font=("Bahnschrift SemiBold SemiConden",16))
        self.latitude_box.place(x=165,y=40)

        self.latitude_value = CTkLabel(main_outdoor_box,width=130,height=80,bg_color="grey10",text='',text_color="white",
                                   font=("Bahnschrift SemiBold SemiConden",35))
        self.latitude_value.place(x=165,y=85)
        
        # Longitude box
        self.longitude_box = CTkLabel(main_outdoor_box,width=130,height=40,bg_color="grey10",text='Longitude',text_color="white",
                                   font=("Bahnschrift SemiBold SemiConden",16))
        self.longitude_box.place(x=307,y=40)

        self.longitude_value = CTkLabel(main_outdoor_box,width=130,height=80,bg_color="grey10",text='',text_color="white",
                                   font=("Bahnschrift SemiBold SemiConden",35))
        self.longitude_value.place(x=307,y=85)

        # altitude box
        self.altitude_box = CTkLabel(main_outdoor_box,width=130,height=40,bg_color="grey10",text='Altitude',text_color="white",
                                   font=("Bahnschrift SemiBold SemiConden",16))
        self.altitude_box.place(x=450,y=40)

        self.altitude_value = CTkLabel(main_outdoor_box,width=130,height=80,bg_color="grey10",text='',text_color="white",
                                   font=("Bahnschrift SemiBold SemiConden",35))
        self.altitude_value.place(x=450,y=85)

        self.update_ram_used()
        # self.update_gpu_name()
        # self.gpu_persentage()
        # self.gpu_used()
        
        
    

    def update_ram_used(self):
        
        virtual_memory = psutil.virtual_memory()
        percent_used = virtual_memory.percent
        self.ram_number.configure(text=f'{percent_used} %')
        
        self.ram_number.after(1010, self.update_ram_used)
            
    # def update_gpu_name(self):
    #     gpu = GPUtil.getGPUs()
    #     namagpu = gpu[0].name  
    #     self.gpu_name.configure(text=f'{namagpu}')
        

    # def gpu_persentage(self):
    #     gpu = GPUtil.getGPUs()
    #     used_persentage = gpu[0].load * 100
    #     self.GpuLoadName.configure(text=f'{used_persentage} %')
    #     self.GpuLoadName.after(1020,self.gpu_persentage)
        
    # def gpu_used(self):
    #     gpu = GPUtil.getGPUs()
    #     vram_used = gpu[0].memoryUsed
    #     vram_total = gpu[0].memoryTotal
    #     persentase_vram_used = (vram_used / vram_total) * 100
    #     self.GPUVRAMNAME.configure(text=f'{round(persentase_vram_used, 2)} %')
    #     self.GPUVRAMNAME.after(1040,self.gpu_used)




class Page1(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.script_dir = os.path.dirname(os.path.abspath(__file__))

        # self.__data1 = VideoData()
        
        background = CTkLabel(self,width=1280,height=720,text='',bg_color="grey20")
        background.place(x=0,y=0)


        self.is_running = False 
        self.elapsed_time = timedelta()

        self.time_var = StringVar()
        self.time_var.set(self.format_time(self.elapsed_time))



        side_bar = CTkCanvas(background, width=150,
                                    height=1490, 
                                    bg="gray10",
                                    highlightthickness=0
                                    )
        side_bar.place(x=0,y=0)

        image_home = os.path.join(self.script_dir, 'app_asset', 'home.png')
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

        camera_logo_path = os.path.join(self.script_dir, 'app_asset', 'kamera2.png')
        imagehome = CTkImage(light_image=Image.open(camera_logo_path), size=(45,45))
        image_camera = CTkLabel(background,image=imagehome,text='',bg_color='grey20',width=100, height=100)
        image_camera.place(x=-12,y=150)

        camera_logo_path = os.path.join(self.script_dir, 'app_asset', 'map.png')
        imagehome = CTkImage(light_image=Image.open(camera_logo_path), size=(55,55))
        image_camera = CTkLabel(side_bar,image=imagehome,text='',bg_color='grey10',width=100, height=100)
        image_camera.place(x=-12,y=260)

        camera_logo_path = os.path.join(self.script_dir, 'app_asset', 'document1.png')
        imagehome = CTkImage(light_image=Image.open(camera_logo_path), size=(55,55))
        image_camera = CTkLabel(side_bar,image=imagehome,text='',bg_color='grey10',width=100, height=100)
        image_camera.place(x=-12,y=370)

        #======================================== SIDE BOX SECTION ====================================================#
        
        
        sidebox = CTkLabel(background,height=542, width=210,text="",bg_color="grey10")
        sidebox.place(x=1060, y = 10)
        
        # JUDUL KOTAK SAMPING
        title_sidebox = CTkLabel(sidebox,bg_color="grey10",text='Video Data',font=("Bahnschrift SemiBold SemiConden",16),text_color='white')
        title_sidebox.place(x=74, y = 5)

        countbox = CTkLabel(sidebox,bg_color="grey20",text='',width=200,height=100)
        countbox.place(x=5, y = 50)

        numberbox = CTkLabel(countbox,bg_color="grey20",text='Pothole Counter',font=("Bahnschrift SemiBold SemiConden",14),text_color="white")
        numberbox.place(x=55, y = 2)

        self.counter_pothole = CTkLabel(countbox,bg_color="gray10",text='0',width=190,height=60,font=("Bahnschrift SemiBold SemiConden",24),text_color="white")
        self.counter_pothole.place(x=5, y = 35)

        # Latitude longitude

        latbox = CTkLabel(sidebox,bg_color="grey20",text='',width=200,height=150)
        latbox.place(x=5, y = 160)

        location_box = CTkLabel(latbox,bg_color="grey20",text='Location',font=("Bahnschrift SemiBold SemiConden",14),text_color="white")
        location_box.place(x=75, y = 2)

        self.latitude = CTkLabel(latbox,bg_color="grey20",text='Latitude\t\t = - °E',font=("Bahnschrift SemiBold SemiConden",14),text_color="white")
        self.latitude.place(x=5, y = 30)

        self.longitude = CTkLabel(latbox,bg_color="grey20",text='Longitude\t\t = - °N',font=("Bahnschrift SemiBold SemiConden",14),text_color="white")
        self.longitude.place(x=5, y = 50)

        self.altimeter = CTkLabel(latbox,bg_color="grey20",text='Altitude\t\t = - m asl',font=("Bahnschrift SemiBold SemiConden",14),text_color="white")
        self.altimeter.place(x=5, y = 70)

        self.suhu = CTkLabel(latbox,bg_color="grey20",text='Temperature\t = - °C',font=("Bahnschrift SemiBold SemiConden",14),text_color="white")
        self.suhu.place(x=5, y = 90)

        # DURATION BOX 
        
        durationbox = CTkLabel(sidebox,bg_color="grey20",text='',width=200,height=95)
        durationbox.place(x=5, y = 320)

        duration_title = CTkLabel(durationbox,bg_color="grey20",text='Detection Duration',font=("Bahnschrift SemiBold SemiConden",14),text_color="white")
        duration_title.place(x=50, y = 2)

        self.duration = CTkLabel(durationbox,bg_color="gray10",textvariable=self.time_var,width=190,height=50,font=("Bahnschrift SemiBold SemiConden",24),text_color="white")
        self.duration.place(x=5, y = 35)


        # ======================================== BOTTOM BOX ================================================#

        bottombox = CTkLabel(background,height=143, width=1185,text="",bg_color="grey10")
        bottombox.place(x=85, y = 565)

        self.videobox = CTkCanvas(background, width=1920, height=1080,bg="grey10")
        self.videobox.place(x=170,y=20) 

        #========================================= VIDEO SECTION =======================================================#

        # video_canvas = CTkCanvas(self,w)

        self.photo = None
        self.stopped = False
        

        playbox = CTkLabel(bottombox, width=390, height=120,bg_color='gray20',text='')
        playbox.place(x=12,y=12)

        textbox = CTkLabel(playbox, text_color='white',font=("Bahnschrift SemiBold SemiConden",14),text="Video Control",bg_color='grey20',)
        textbox.place(x=160,y=1)

        input = CTkLabel(bottombox, width=390, height=120,bg_color='grey20',text='')
        input.place(x=410,y=12)

        inputtextbox = CTkLabel(input, text_color='white',font=("Bahnschrift SemiBold SemiConden",14),text="Video Source",bg_color='grey20',)
        inputtextbox.place(x=160,y=1)

        self.file_name = CTkLabel(input, text_color='white',font=("Bahnschrift SemiBold SemiConden",14),text=f"path : ",bg_color='grey20',)
        self.file_name.place(x=100,y=30)

        self.checkbox_var = BooleanVar()
        self.checkbox1 = CTkCheckBox(input, text="File Source",border_color="white", variable=self.checkbox_var, command=self.on_checkbox_change,font=("Bahnschrift SemiBold SemiConden",14),bg_color="grey20",text_color="white")
        self.checkbox1.place(x=265,y=35)
        
        
        self.manual_input = CTkTextbox(input,height=12,width=200,font=("Bahnschrift SemiBold SemiConden",14),bg_color="grey20",text_color="White",fg_color="grey")
        self.manual_input.place(x=10 ,y= 65)
        self.manual_input.configure(state="disabled")

        self.checkbox_var_manual = BooleanVar()
        self.checkbox2 = CTkCheckBox(input, text="Manual Source", variable=self.checkbox_var_manual, 
                                     command=self.on_checkbox_change,font=("Bahnschrift SemiBold SemiConden",14),
                                     bg_color="grey20",text_color="white",border_color="white")
        self.checkbox2.place(x=265,y=70)


        self.file_input = CTkButton(input, 
                                 text='Select File',
                                 command=(self.select_file),
                                 fg_color='grey30',
                                 hover_color="#fce101",
                                 width=80,
                                 height=20,
                                 font=("Bahnschrift SemiBold SemiConden",14),
                                 bg_color="grey20"
                                
                                 )
        self.file_input.place(x=10, y=35)
        self.file_input.configure(state="disabled")

        play_logo = os.path.join(self.script_dir, 'app_asset', 'play.png')
        imagelogo = CTkImage(light_image=Image.open(play_logo), size=(45,45))
        start_button = CTkButton(playbox, 
                                 text='START DETECTION',
                                 command=(self.start_detection),
                                 fg_color='grey30',
                                 hover_color="#228B22",
                                 width=180,
                                 height=75,
                                 image=imagelogo,
                                 font=("Bahnschrift SemiBold SemiConden",14),
                                 bg_color="grey20"
                                 )
        start_button.place(x=10, y=35)

        stop_logo = os.path.join(self.script_dir, 'app_asset', 'stop2.png')
        imagestop = CTkImage(light_image=Image.open(stop_logo), size=(45,45))
        stop_button = CTkButton(playbox, 
                                 text='STOP DETECTION',
                                 command=self.stop_detection,
                                 fg_color='grey30',
                                 hover_color="#FF0000",
                                 width=180,
                                 height=75,
                                 image=imagestop,
                                 font=("Bahnschrift SemiBold SemiConden",14),bg_color="grey20"
                                 )
        stop_button.place(x=200, y=35)

        self.data = {}

        # Untuk File handler csv

        select_folder = CTkLabel(bottombox, width=360, height=120,bg_color='grey20',text='')
        select_folder.place(x=810,y=12)

        select_foldertextbox = CTkLabel(select_folder, text_color='white',font=("Bahnschrift SemiBold SemiConden",14),text="Save Data",bg_color='grey20',)
        select_foldertextbox.place(x=155,y=1)

        self.folderinput = CTkButton(select_folder, 
                                 text='Select Folder',
                                 command=self.select_folder,
                                 fg_color='grey30',
                                 hover_color="#fce101",
                                 width=80,
                                 height=20,
                                 font=("Bahnschrift SemiBold SemiConden",14),
                                 bg_color="grey20"
                                
                                 )
        self.folderinput.place(x=10, y=35)
        self.file_input.configure(state="disabled")

        self.folder_name = CTkLabel(select_folder, text_color='white',font=("Bahnschrift SemiBold SemiConden",14),text=f"path : ",bg_color='grey20',)
        self.folder_name.place(x=100,y=30)

        self.checkbox_var_save = BooleanVar()
        self.save = CTkCheckBox(select_folder, text="Save cropped", variable=self.checkbox_var_save,font=("Bahnschrift SemiBold SemiConden",14),
                                bg_color="grey20",text_color="white",hover_color="#fce101",border_color="white")
        self.save.place(x=235,y=34)

        self.folder_file_name = CTkEntry(select_folder,height=24,width=250,font=("Bahnschrift SemiBold SemiConden",14),
                                         placeholder_text="",text_color="white",bg_color="grey",fg_color="grey20")
        self.folder_file_name.place(x=9 ,y= 87)

        self.nameinputfolder = CTkLabel(select_folder, text_color='white',font=("Bahnschrift SemiBold SemiConden",13),text="Input name for folder and data file",bg_color='grey20',)
        self.nameinputfolder.place(x=10,y=58)


        # Outdoor status 
        

    # Format Time ============================================
    def update_time(self):
        if self.is_running:
            self.elapsed_time += timedelta(milliseconds=100)
            self.time_var.set(self.format_time(self.elapsed_time))
            self.duration.after(100, self.update_time)
        else:
            self.duration.after_cancel(self.update_time)
    
    
    def format_time(self, elapsed_time):
        milliseconds = int(elapsed_time.total_seconds() * 1000)
        minutes, seconds = divmod(milliseconds // 1000, 60)
        return f"{minutes:02d}:{seconds:02d}.{milliseconds % 1000 // 10:02d}"

    
    def on_checkbox_change(self):
        
        if self.checkbox_var.get():
            # Checkbox is checked, enable the button
            self.checkbox_var_manual.set(False)
            self.file_input.configure(state="normal")
            self.manual_input.configure(state="disabled")
            
        elif self.checkbox_var_manual.get():
            # Checkbox is unchecked, disable the button
            self.checkbox_var.set(False)
            self.file_input.configure(state="disabled")
            self.manual_input.configure(state="normal")

        else :
            self.checkbox_var.set(False)
            self.checkbox_var_manual.set(False)
            self.file_input.configure(state="disabled")
            self.manual_input.configure(state="disabled")


    
    def select_file(self):

        self.filename_var = tk.StringVar()

        filetypes = (
            ('MP4 files', '*.mp4'),
            ('AVI files', '*.avi'),
            ('MKV files', '*.mkv'),
            ('All files', '*.*')
        )

        self.filename = filedialog.askopenfilename(
            title='Open a file',
            initialdir=self.script_dir,
            filetypes=filetypes
            )
        
        self.filename_var.set(os.path.basename(self.filename))
        self.file_name.configure(text=f"Path : {self.filename_var.get()}")
        # print(self.filename_var)

    def select_folder(self):

        self.foldername_var = StringVar()

        self.foldername = filedialog.askdirectory(title="Select Folder to Save",
                                                  initialdir=self.script_dir)
        
        self.foldername_var.set(os.path.basename(self.foldername))
        self.folder_name.configure(text=f"Path : {self.foldername_var.get()}")
        
        
    def crop_image(self,img, id):
        
        x = datetime.datetime.now()

        # folder_title = str(f"{self.folder_file_name.get()}_potholeimage")
        # main_path = f"{str(self.foldername)}"  
        # main_folder = os.path.join(main_path, folder_title)

        # if not os.path.exists(main_folder):
        #     os.makedirs(main_folder)

        parent_folder = str(self.foldername)
        self.new_folder = os.path.join(parent_folder,f'{self.folder_file_name.get()}_folder')

        if not os.path.exists(self.new_folder) :
            os.makedirs(self.new_folder)

        file_name = f'{id}_{x.hour}_{x.minute}_{x.second}_{x.microsecond}.png'
        self.image_path = os.path.join(self.new_folder, file_name)
        cv2.imwrite(self.image_path, img)
        
    def on_start(self):
        
        if not self.is_running:
            self.is_running = True
            self.update_time()

        
        self.file_input.configure(state="disabled")
        self.manual_input.configure(state="disabled")
        self.folderinput.configure(state="disabled")
        self.save.configure(state="disabled")
        self.checkbox1.configure(state="disabled")
        self.checkbox2.configure(state="disabled")
        self.folder_file_name.configure(state="disabled")
    

    def start_detection(self):

        input_content = self.folder_file_name
        if not input_content.get():
             error_message = "File and Folder name is Empty"
             CTkMessagebox(self,title="Error",message=error_message, height=200,width=400,icon="warning",
                          font=("Bahnschrift SemiBold SemiConden",14),bg_color="grey20")
             
             return
        
        self.on_start()
        
        self.stopped = False
        model = YOLO(os.path.join(self.script_dir, 'custom.pt'))
        # self.cap = cv2.VideoCapture("test2.mp4")

        try :
            if self.checkbox_var.get():
                cap = cv2.VideoCapture(self.filename)
               
            else:
                cap = cv2.VideoCapture(int(self.manual_input.get(1.0, "end-1c")))
             

        except Exception as e :
            error_message = "Video Source Is Empty"
            CTkMessagebox(self,title="Error",message=error_message, height=200,width=400,icon="warning",
                          font=("Bahnschrift SemiBold SemiConden",14))
            return
            
        my_file = open(os.path.join(self.script_dir, 'coco.txt'), "r")
        data = my_file.read()
        class_list = data.split("\n")

        count = 0
        tracker = Tracker()
        # lat, long = curr_loc.coordinates()

        
        # day, date, hour = curr_loc.time_stamp()
        # lat, long = curr_loc.coordinates()
        

        
        lat, long = curr_loc.coordinates()
        temprature,elevation = curr_loc.temprature_data(lat,long)
        data, counter1 = {}, []
        coord_y_line1, offset = 700, 40
        width, height = {}, {}

        

        def update_frame():
            nonlocal count
            nonlocal cap
            nonlocal model

            if self.stopped == True:
                cap.release()
                return
            
            ret, frame = cap.read()
            if not ret :
                return

            count += 1
            if count % 3 != 0:
                self.videobox.after(10, update_frame)
                return

            frame = cv2.resize(frame, (1920,1080))

            results = model.predict(frame)
            a = results[0].boxes.data
            px = pd.DataFrame(a).astype("float")
            pothole_list = []

            for index, row in px.iterrows():
                x1, y1, x2, y2, _, d = map(int, row)
                c = class_list[d]
                if 'pothole' in c:
                    pothole_list.append([x1, y1, x2, y2])

            bbox_id = tracker.update(pothole_list)
            for bbox in bbox_id:
                 
                x3, y3, x4, y4, id = bbox
                cx, cy = int(x3 + x4) // 2, int(y3 + y4) // 2
                cv2.circle(frame, (cx, cy), 2, (255, 0, 255), -1)

                if coord_y_line1 < (cy + offset) and coord_y_line1 > (cy - offset):
                    cv2.rectangle(frame, (x3, y3), (x4, y4), (0, 255, 0), 5)
                    cvzone.putTextRect(frame, f'id: {id} {c}', (x3, y3), 1, 1)
                    if counter1.count(id) == 0:

                        day, date, hour = curr_loc.time_stamp()
                        
                        
                        
                        width = round((x2 - x1) * 0.1949152542, 2)  # predict width
                        height = round((y2 - y1) * 0.11392405, 2)  # predict height
                        cv2.putText(frame, f'Width: {width}cm', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                    (0, 0, 255), 2)
                        cv2.putText(frame, f'Height: {height}cm,', (x1, y1 - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                    (0, 0, 255), 2)
                        crop = frame[y3:y4, x3:x4]

                        if self.checkbox_var_save.get():
                            self.crop_image(crop, id)

                        counter1.append(id)
                        self.data[id] = {
                            'Latitude': lat,
                            'Longtitude': long,
                            'Day': day,
                            'Date': date,
                            'Time': hour,
                            'Width': width,
                            'height': height,
                            'Elevation' : elevation,
                            "temprature" : temprature
                        }

            
            self.latitude.configure(text=f'Latitude\t\t = {lat} °E')
            self.longitude.configure(text=f'Longitude\t\t = {long} °N')

            cv2.line(frame, (3, coord_y_line1), (1920, coord_y_line1), (0, 225, 225), 5)

            cv2.putText(frame, text=f'Temp = {len(counter1)}', org=(30, 450),
                        fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=0.7,
                        color=(0, 255, 0), thickness=1)
            
            self.counter_pothole.configure(text=f'{len(counter1)}')
            self.altimeter.configure(text=f"Altitude\t\t = {elevation} m asl")
            self.suhu.configure(text=f"temperature\t = {round(temprature,2)} °C")

            cv2.putText(frame, text='Screening Line', org=(10, 600),
                        fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=1,
                        color=(0, 255, 0), thickness=2)

            # cv2.putText(frame, text=f'Loc = {lat, long}', org=(10, 380),
            #             fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=0.5,
            #             color=(0, 255, 0), thickness=1)

            

            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            self.photo =  ImageTk.PhotoImage(image=Image.fromarray(rgb_frame))
            self.videobox.create_image(0, 0, anchor=tk.NW, image=self.photo)

            self.videobox.after(10, update_frame)

           
        
        if not self.stopped:
            self.videobox.after(10, update_frame)
    

    def on_stop(self):

        if self.is_running:
            self.is_running = False
            self.elapsed_time = timedelta()
            self.time_var.set(self.format_time(self.elapsed_time))

        self.file_input.configure(state="normal")
        self.manual_input.configure(state="normal")
        self.folderinput.configure(state="normal")
        self.save.configure(state="normal")
        self.checkbox1.configure(state="normal")
        self.checkbox2.configure(state="normal")
        self.folder_file_name.configure(state="normal")
        self.counter_pothole.configure(text='0')
        self.latitude.configure(text='Latitude\t\t = - °E')
        self.longitude.configure(text='Longitude\t\t = - °N')
        self.altimeter.configure(text=f"Altitude\t\t = - m asl")
        self.suhu.configure(text=f"temperature\t = - °C")

    def stop_detection(self):

        self.stopped = True
        self.videobox.delete("all")
        self.on_stop()

        if self.data:
            
            parent_folder = str(self.foldername)
            self.new_folder = os.path.join(parent_folder,f'{self.folder_file_name.get()}_folder')

            if not os.path.exists(self.new_folder) :
                os.makedirs(self.new_folder)

            df = pd.DataFrame.from_dict(self.data, orient='index')
            csv_filename = os.path.join(self.new_folder, f'{self.folder_file_name.get()}'+'.csv')
            df.to_csv(csv_filename, index_label='ID')
            success_message = f'Data saved to {csv_filename}'
            CTkMessagebox(self, title="Success", message=success_message, height=200, width=400, icon="info",
                        font=("Bahnschrift SemiBold SemiConden", 14))
            



class Page2(ctk.CTkFrame,CTk):
    def __init__(self, parent, controller):
        super().__init__(parent)

        background = CTkLabel(self,width=1280,height=720,text='',bg_color="grey20")
        background.place(x=0,y=0)



        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        side_bar = CTkCanvas(background, width=150,
                                    height=1490, 
                                    bg="gray10",
                                    highlightthickness=0,
                                    )
        side_bar.place(x=0,y=0)

        image_home = os.path.join(self.script_dir, 'app_asset', 'home.png')
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

       
        camera_logo_path = os.path.join(self.script_dir, 'app_asset', 'kamera2.png')
        imagehome = CTkImage(light_image=Image.open(camera_logo_path), size=(45,45))
        image_camera = CTkLabel(side_bar,image=imagehome,text='',bg_color='grey10',width=100, height=100)
        image_camera.place(x=-12,y=150)

        camera_logo_path = os.path.join(self.script_dir, 'app_asset', 'map.png')
        imagehome = CTkImage(light_image=Image.open(camera_logo_path), size=(55,55))
        image_camera = CTkLabel(side_bar,image=imagehome,text='',bg_color='grey20',width=100, height=100)
        image_camera.place(x=-12,y=260)

        camera_logo_path = os.path.join(self.script_dir, 'app_asset', 'document1.png')
        imagehome = CTkImage(light_image=Image.open(camera_logo_path), size=(55,55))
        image_camera = CTkLabel(side_bar,image=imagehome,text='',bg_color='grey10',width=100, height=100)
        image_camera.place(x=-12,y=370)


        # JUDUL KOTAK SAMPING 
        sidebox = CTkLabel(background,height=695, width=210,text="",bg_color="grey10")
        sidebox.place(x=1060, y = 10)

        title_sidebox = CTkLabel(sidebox,bg_color="grey10",text='Map Configuration',font=("Bahnschrift SemiBold SemiConden",16),text_color='white')
        title_sidebox.place(x=50, y = 5)

        
        box_file_hander_map_csv = CTkLabel(sidebox,bg_color="grey20",text='',width=200,height=170)
        box_file_hander_map_csv.place(x=5, y = 45)

        title_handler_map_csv = CTkLabel(box_file_hander_map_csv,bg_color="grey20",text='CSV Handler',font=("Bahnschrift SemiBold SemiConden",14),text_color="white")
        title_handler_map_csv.place(x=65, y = 5)


        
        self.map_containter = CTkLabel(background,width=960,height=695,text="Click Start to show map",bg_color="grey10",text_color="white")
        self.map_containter.place(x=90,y=12)
    
        #  MAP SEGMENTATION ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        title_handler_map_csv = CTkLabel(sidebox,bg_color="grey10",text='Start/Stop Showing Map',font=("Bahnschrift SemiBold SemiConden",14),text_color="white")
        title_handler_map_csv.place(x=40, y = 230)


        # START / STOP SHOWING MAP 
        self.startMap_Button = CTkButton(sidebox,height=100,width=90, text="START",command=self.start_map,fg_color="#228B22",
                                    hover_color="#fce101",font=("Bahnschrift SemiBold SemiConden",18),bg_color="grey20")
        self.startMap_Button.place(x=10,y=270)


        self.stopMap_Button = CTkButton(sidebox,height=100,width=90, text="STOP",command=self.stop_map,fg_color="grey50",
                                        hover_color="#fce101",font=("Bahnschrift SemiBold SemiConden",18),bg_color="grey20")
        self.stopMap_Button.place(x=110,y=270)
        self.stopMap_Button.configure(state='disabled')


        self.choose_csv = CTkButton(box_file_hander_map_csv,height=40,width=190, 
                               text="Select CSV",
                               fg_color="grey50",
                               hover_color="#fce101",
                               font=("Bahnschrift SemiBold SemiConden",16),
                                text_color="grey10",
                               command=self.select_csv,
                               bg_color="grey20"
                               )
        
        self.choose_csv.place(x=5,y=40)

        title_csv_path = CTkLabel(sidebox,bg_color="grey20",text='CSV Path',font=("Bahnschrift SemiBold SemiConden",12),text_color='white')
        title_csv_path.place(x=12, y = 125)

        self.csv_path = CTkButton(box_file_hander_map_csv,width=190,height=40,text='',fg_color="grey50",
                                  font=("Bahnschrift SemiBold SemiConden",16),bg_color="grey20",
                                 state="disabled")
        self.csv_path.place(x=5,y=110)

        self.path_name = CTkLabel(self.csv_path,text="", font=("Bahnschrift SemiBold SemiConden",12),
                                  text_color="grey10",bg_color="transparent")
        self.path_name.place(x=10,y=5)

        # FIND DETAIL MAP DATA =======================================================================

        title_detail_map = CTkLabel(sidebox,bg_color="grey10",text='Find Detail Point ID',font=("Bahnschrift SemiBold SemiConden",14),text_color="white")
        title_detail_map.place(x=50, y = 390)

        self.find_id = CTkEntry(sidebox,height=30,width=150,placeholder_text="input ID to find detail",bg_color="grey20",text_color="white",fg_color="grey30")
        self.find_id.place(x=10 ,y=420)
        self.find_id.configure(state='disabled')

        search_logo_path = os.path.join(self.script_dir, 'app_asset', 'cari.png')
        search_logo = CTkImage(light_image=Image.open(search_logo_path), size=(20,20))
        self.find_button = CTkButton(sidebox,height=30,width=30,fg_color="grey50",font=("Bahnschrift SemiBold SemiConden",12),
                                image=search_logo,text='',command=self.location_detail,bg_color="grey20")
        self.find_button.place(x=165, y=420)
        self.find_button.configure(state='disabled')



        self.ID_detail = CTkButton(sidebox,width=190,height=170,text='',fg_color="grey50",bg_color="grey20",
                                  font=("Bahnschrift SemiBold SemiConden",16),
                                 state="disabled")
        self.ID_detail.place(x=10,y=460)

        

        # ID DETAIL TEXT ==================================================

        self.ID_value = CTkButton(self.ID_detail,width=185,height=35,text='-',fg_color="grey10",
                                  font=("Bahnschrift SemiBold SemiConden",22),
                                 state="disabled")
        self.ID_value.place(x=2,y=2)
        
        self.day_value = CTkLabel(self.ID_detail,text="Day\t=", font=("Bahnschrift SemiBold SemiConden",14),height=14,
                                  text_color="white",bg_color="transparent")
        self.day_value.place(x=7,y=40)

        self.time_value = CTkLabel(self.ID_detail,text="Time\t=", font=("Bahnschrift SemiBold SemiConden",14),height=14,
                                  text_color="white",bg_color="transparent")
        self.time_value.place(x=7,y=60)

        self.width_value = CTkLabel(self.ID_detail,text="Width\t=", font=("Bahnschrift SemiBold SemiConden",14),height=14,
                                  text_color="white",bg_color="transparent")
        self.width_value.place(x=7,y=80)

        self.lenght_value = CTkLabel(self.ID_detail,text="Lenght\t=", font=("Bahnschrift SemiBold SemiConden",14),height=14,
                                  text_color="white",bg_color="transparent")
        self.lenght_value.place(x=7,y=100)

        self.latitude_value = CTkLabel(self.ID_detail,text="Lat\t=", font=("Bahnschrift SemiBold SemiConden",14),height=14,
                                  text_color="white",bg_color="transparent")
        self.latitude_value.place(x=7,y=120)

        self.longitude_value = CTkLabel(self.ID_detail,text="Long\t=", font=("Bahnschrift SemiBold SemiConden",14),height=14,
                                  text_color="white",bg_color="transparent")
        self.longitude_value.place(x=7,y=140)

        # self.alamat_value = CTkLabel(self.ID_detail,text="Long\t=", font=("Bahnschrift SemiBold SemiConden",14),height=14,
        #                           text_color="white",bg_color="transparent")
        # self.alamat_value.place(x=7,y=160)

        self.button_show = CTkButton(sidebox,height=40,width=140,command=self.photo_detail,
                                     text="Show Pothole Image",fg_color="grey50",text_color="white",
                                     font=("Bahnschrift SemiBold SemiConden",14),bg_color="grey20"
                                     )
        self.button_show.place(x=10,y=640)
        self.button_show.configure(state="disabled")

        self.indicator_button_show = CTkButton(sidebox,height=40,width=40,text='',state='disabled',bg_color="grey")
        self.indicator_button_show.place(x=160,y=640)
        self.indicator_button_show.configure(fg_color="#FF0000")

        self.empty_field()
    
       


    def start_map(self):
        self.after(2000,self.map_handler)
        self.startMap_Button.configure(fg_color="grey50",state='disabled')
        self.stopMap_Button.configure(fg_color="#FF0000",state='normal')
        self.choose_csv.configure(state='disabled')

        # self.map_handler()


    def empty_field (self) :
        '''
        This code for clear the parameter if stop button was pressed
        '''
        self.ID_value.configure(text=f"-")
        self.latitude_value.configure(text=f"Lat\t= - °E")
        self.longitude_value.configure(text=f"Long\t= - °N")
        self.day_value.configure(text=f"Day\t= - , -")
        self.time_value.configure(text=f"Time\t= - ")
        self.width_value.configure(text=f"Width\t= - cm")
        self.lenght_value.configure(text=f"Lenght\t= - cm")

    def stop_map(self):
        self.map_widget.destroy()
        self.startMap_Button.configure(fg_color="#228B22",state='normal')
        self.stopMap_Button.configure(fg_color="grey50",state='disabled')
        self.button_show.configure(state="disabled")
        self.find_button.configure(state='disabled')
        self.find_id.configure(state="disabled")
        self.indicator_button_show.configure(fg_color="#FF0000")
        self.choose_csv.configure(state='normal')

        self.empty_field()

    def map_handler(self):
        
        # Pandas Handler =================================================

        try :
            self.map_widget = tkmap.TkinterMapView(self.map_containter,width=1890,height=1360)
            self.map_widget.place(x=15,y=15)

            self.data = pd.read_csv(self.filename_csv)
            self.data[['ID', 'Latitude', 'Longtitude']]

            for index,row in self.data.iterrows():
                id = row['ID']
                latitude = row['Latitude']
                longitude = row['Longtitude']

                # print(f"{latitude},{longitude}")
                self.map_widget.set_position(latitude, longitude,marker=True,text=f"{id}")

            self.find_id.configure(state="normal")
            self.find_button.configure(state="normal")
            # self.indicator_button_show.configure(fg_color="#228B22")
            

           
        except Exception :
            self.stop_map()
            CTkMessagebox(self,title="error",icon="cancel",message="CSV File cannot read",height=40,width=100)
            self.startMap_Button.configure(fg_color="#228B22",state='normal')
            self.stopMap_Button.configure(fg_color="grey50",state='disabled')
            # self.indicator_button_show.configure(fg_color="#FF0000")
            # print(e)
            
    def location_detail(self):
        # selected_row = self.data[self.data['ID'] == int(self.find_id.get()) ]
        # Date	Time	Width	height	Elevation	temprature

        try:
            id = self.data.loc[self.data['ID'] == int(self.find_id.get()) , 'ID'].values[0]
            latitude = self.data.loc[self.data['ID'] == int(self.find_id.get()) , 'Latitude'].values[0]
            longitude = self.data.loc[self.data['ID'] == int(self.find_id.get()) , 'Longtitude'].values[0]
            day = self.data.loc[self.data['ID'] == int(self.find_id.get()) , 'Day'].values[0]
            date = self.data.loc[self.data['ID'] == int(self.find_id.get()) , 'Date'].values[0]
            time = self.data.loc[self.data['ID'] == int(self.find_id.get()) , 'Time'].values[0]
            width = self.data.loc[self.data['ID'] == int(self.find_id.get()) , 'Width'].values[0]
            height = self.data.loc[self.data['ID'] == int(self.find_id.get()) , 'height'].values[0]
            # elevation = selected_row['Elevation']
            # temp = selected_row['temprature']

            self.ID_value.configure(text=f"{id}")
            self.latitude_value.configure(text=f"Lat\t= {latitude} °E")
            self.longitude_value.configure(text=f"Long\t= {longitude} °N")
            self.day_value.configure(text=f"Day\t= {day}, {date}")
            self.time_value.configure(text=f"Time\t= {time}")
            self.width_value.configure(text=f"Width\t= {width} cm")
            self.lenght_value.configure(text=f"Lenght\t= {height} cm")

            # adr = tkmap.convert_coordinates_to_address(latitude,longitude)
            # listadr = adr.street,adr.housenumber,adr.postal,adr.city,adr.state,adr.country
            # wrapper = textwrap.TextWrapper(width=30)
            # word_list = wrapper.wrap(text=listadr)
            

            folder_path = str(self.folder_name_csv)  # Replace this with the actual path to your folder
            files_in_folder = os.listdir(folder_path)

            matching_files = [file for file in files_in_folder if self.extract_prefix(file) == str(self.find_id.get()) and file.endswith(".png")]
            
            '''
            Code below for find if there any csv file that matching with id wanna to
            search then on the button and confirm gave signal indicator to greeen, that 
            indicate file .png that id find available and ready to show.

            '''


            if not matching_files:
                self.button_show.configure(state="disabled")
                self.indicator_button_show.configure(fg_color="#FF0000")
                # self.empty_field()
                return
            
            else :
                self.button_show.configure(state="normal")
                self.indicator_button_show.configure(fg_color="#228B22")


            # self.alamat_value.configure(text=f"{word_list}")

        except Exception as e :
            CTkMessagebox(self,title="error",icon="cancel",message="ID not found",height=40,width=100)
            self.button_show.configure(state="disabled")
            self.indicator_button_show.configure(fg_color="#FF0000")
            self.empty_field()

    def extract_prefix(self, filename):
        # Extract the part of the file name before the first underscore
            parts = filename.split('_')
            if parts:
                return parts[0]
            return ''
    
    def photo_detail(self):
        folder_path = str(self.folder_name_csv)  # Replace this with the actual path to your folder
        # files_in_folder = os.listdir(folder_path)
        # if not any(file.endswith('.png') for file in files_in_folder):
        #     print(f"Error: No .png files found in {folder_path}")
        #     return
        # else :
        prefix_to_match = int(self.find_id.get())

        photo_detail_window = PhotoDetailWindow(self, folder_path, prefix_to_match)
        photo_detail_window.focus()

        # List all files in the folder
        # files_in_folder = os.listdir(folder_path)

        # # Filter files that match the condition (start with "18" and have the ".png" extension)
        # matching_files = [file for file in files_in_folder if file.startswith(prefix_to_match) and file.endswith(".png")]

        # # Print the matching files
        # for file in matching_files:
        #     file_path = os.path.join(folder_path,file)
        #     image = Image.open(file_path)
        #     photo = CTkImage(light_image=image, size=(45,45))

        #     top = CTkToplevel(self)
        #     top.title(prefix_to_match)

        #     photo_label = CTkLabel(top,image=photo)
        #     photo_label.pack()


    
    def select_csv(self):

        self.filename_var = tk.StringVar()

        filetypes = (('CSV files', '*.csv'), 
                     ('All files', '*.*'))

        self.filename_csv = filedialog.askopenfilename(
            title='Open a file',
            initialdir=self.script_dir,
            filetypes=filetypes
            )
        
        self.filename_var.set(os.path.basename(self.filename_csv))
        self.path_name.configure(text=f"{self.filename_var.get()}")

        self.folder_name_csv = os.path.dirname(self.filename_csv)
        

class PhotoDetailWindow(ctk.CTkToplevel):
    def __init__(self, master, folder_path, prefix_to_match):
        super().__init__(master)
        self.title(f"ID_{prefix_to_match}")
        
        self.resizable(False,False)

        files_in_folder = os.listdir(folder_path)

        # Filter files that match the condition (start with the specified prefix and have the ".png" extension)
        matching_files = [file for file in files_in_folder if self.extract_prefix(file) == str(prefix_to_match) and file.endswith(".png")]
        
        if not matching_files:
            return

        # Display matching images
        for file in matching_files:
            file_path = os.path.join(folder_path, file)
            image = Image.open(file_path)

            width,height = image.size
            photo = ctk.CTkImage(light_image=image, size=(width*2, height*2))

            photo_label = ctk.CTkLabel(self,text='', image=photo,height=100,width=100)
            photo_label.pack(pady=50)

        geo = f"{width*4}x{height*4}"

        self.geometry(geo)

    def extract_prefix(self, filename):
        # Extract the part of the file name before the first underscore
        parts = filename.split('_')
        if parts:
            return parts[0]
        return ''
    
class Page3(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        '''
        Below this variable that use as GUI of front of document page
        '''

        background = CTkLabel(self,width=1280,height=720,text='',bg_color="grey20")
        background.place(x=0,y=0)

        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        side_bar = CTkCanvas(background, width=150,
                                    height=1490, 
                                    bg="gray10",
                                    highlightthickness=0,
                                    )
        side_bar.place(x=0,y=0)
        

        image_home = os.path.join(self.script_dir, 'app_asset', 'home.png')
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

        camera_logo_path = os.path.join(self.script_dir, 'app_asset', 'kamera2.png')
        imagehome = CTkImage(light_image=Image.open(camera_logo_path), size=(45,45))
        image_camera = CTkLabel(side_bar,image=imagehome,text='',bg_color='grey10',width=100, height=100)
        image_camera.place(x=-12,y=150)

        camera_logo_path = os.path.join(self.script_dir, 'app_asset', 'map.png')
        imagehome = CTkImage(light_image=Image.open(camera_logo_path), size=(55,55))
        image_camera = CTkLabel(side_bar,image=imagehome,text='',bg_color='grey10',width=100, height=100)
        image_camera.place(x=-12,y=260)

        camera_logo_path = os.path.join(self.script_dir, 'app_asset', 'document1.png')
        imagehome = CTkImage(light_image=Image.open(camera_logo_path), size=(55,55))
        image_camera = CTkLabel(side_bar,image=imagehome,text='',bg_color='grey20',width=100, height=100)
        image_camera.place(x=-12,y=370)

        '''
        Below this GUI For data visualization
        '''

        total_pothole_box = CTkButton(background,width=240,height=160,text='',fg_color="grey50",
                                  font=("Bahnschrift SemiBold SemiConden",16),corner_radius=6,bg_color="grey20",border_color="white",border_width=3,
                                 state="disabled")
        total_pothole_box.place(x=90,y=15)

        total_width_mean_box = CTkButton(background,width=240,height=160,text='',fg_color="grey50",
                                  font=("Bahnschrift SemiBold SemiConden",16),corner_radius=6,bg_color="grey20",
                                 state="disabled")
        total_width_mean_box.place(x=350,y=15)

        total_lenght_mean_box = CTkButton(background,width=240,height=160,text='',fg_color="grey50",
                                  font=("Bahnschrift SemiBold SemiConden",16),corner_radius=6,bg_color="grey20",
                                 state="disabled")
        total_lenght_mean_box.place(x=610,y=15)

        self.plot_box = CTkTabview(background,height=480,width=760,bg_color="grey20",fg_color="grey10",border_color="white",border_width=2,corner_radius=6)
        self.plot_box.place(x=90,y=190)

        self.plot_box.add("Barplot")
        self.plot_box.add("Heatmap")

        

        
    

    



if __name__ == "__main__":
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    app = tkinterApp()
    app.title('Pothole Detector')
    app.geometry("1280x720")
    app.resizable(False,False)
    
    app.iconbitmap(os.path.join(script_dir, 'app_asset', 'hat.ico'))
    
    app.mainloop()

