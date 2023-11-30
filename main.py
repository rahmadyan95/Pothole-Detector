# import tkinter as tk
# from tkinter import ttk
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
import threading
from customtkinter import filedialog, BooleanVar
from CTkMessagebox import CTkMessagebox
from datetime import timedelta 
from datetime import timedelta
from curr_loc import run_all_functions
import ttkbootstrap as ttk
import psutil


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
        
        # RIGHT SIDE BOX ======================================================================================
        side_background = CTkLabel(self, width=640, height= 468, bg_color="grey",corner_radius=8, text='')
        side_background.place(x=620,y=200)

        title_side = CTkLabel(self,text="SYSTEM INFORMATION", font=("Bahnschrift SemiBold SemiConden",18),text_color="grey10",bg_color="grey")
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

        self.gpu_presentage = CTkLabel(self.GPU_status,width=230,height=95,bg_color="grey10",text='',text_color="white",
                                   font=("Bahnschrift SemiBold SemiConden",35))
        self.gpu_presentage.place(x=10,y=90)

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
        camera_logo_path = os.path.join(os.path.dirname(__file__), 'app_asset\map.png')
        imagehome = CTkImage(light_image=Image.open(camera_logo_path), size=(55,55))
        image_camera = CTkLabel(side_bar,image=imagehome,text='',bg_color='grey10',width=100, height=100)
        image_camera.place(x=-12,y=260)

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

        self.update_meter()

    def update_meter(self):
        virtual_memory = psutil.virtual_memory()
        percent_used = virtual_memory.percent
        self.ram_number.configure(text=f'{percent_used} %')
        self.ram_number.after(1000, self.update_meter)
        


class Page1(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        

        self.is_running = False 
        self.elapsed_time = timedelta()

        self.time_var = StringVar()
        self.time_var.set(self.format_time(self.elapsed_time))



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

        #======================================== SIDE BOX SECTION ====================================================#
        
        
        sidebox = CTkLabel(self,height=542, width=210,text="",bg_color="grey10")
        sidebox.place(x=1060, y = 10)
        
        # JUDUL KOTAK SAMPING
        title_sidebox = CTkLabel(sidebox,bg_color="grey10",text='Video Data',font=("Bahnschrift SemiBold SemiConden",16),text_color='white')
        title_sidebox.place(x=74, y = 5)

        countbox = CTkLabel(sidebox,bg_color="grey20",text='',width=200,height=100)
        countbox.place(x=5, y = 50)

        numberbox = CTkLabel(countbox,bg_color="grey20",text='Pothole Counter',font=("Bahnschrift SemiBold SemiConden",14))
        numberbox.place(x=55, y = 2)

        self.counter_pothole = CTkLabel(countbox,bg_color="gray10",text='0',width=190,height=60,font=("Bahnschrift SemiBold SemiConden",24))
        self.counter_pothole.place(x=5, y = 35)

        # Latitude longitude

        latbox = CTkLabel(sidebox,bg_color="grey20",text='',width=200,height=150)
        latbox.place(x=5, y = 160)

        location_box = CTkLabel(latbox,bg_color="transparent",text='Location',font=("Bahnschrift SemiBold SemiConden",14))
        location_box.place(x=75, y = 2)

        self.latitude = CTkLabel(latbox,bg_color="transparent",text='Latitude\t\t = - °E',font=("Bahnschrift SemiBold SemiConden",14))
        self.latitude.place(x=5, y = 30)

        self.longitude = CTkLabel(latbox,bg_color="transparent",text='Longitude\t\t = - °N',font=("Bahnschrift SemiBold SemiConden",14))
        self.longitude.place(x=5, y = 50)

        self.altimeter = CTkLabel(latbox,bg_color="transparent",text='Altitude\t\t = - m asl',font=("Bahnschrift SemiBold SemiConden",14))
        self.altimeter.place(x=5, y = 70)

        self.suhu = CTkLabel(latbox,bg_color="transparent",text='Temperature\t = - °C',font=("Bahnschrift SemiBold SemiConden",14))
        self.suhu.place(x=5, y = 90)

        # DURATION BOX 
        
        durationbox = CTkLabel(sidebox,bg_color="grey20",text='',width=200,height=95)
        durationbox.place(x=5, y = 320)

        duration_title = CTkLabel(durationbox,bg_color="transparent",text='Detection Duration',font=("Bahnschrift SemiBold SemiConden",14))
        duration_title.place(x=50, y = 2)

        self.duration = CTkLabel(durationbox,bg_color="gray10",textvariable=self.time_var,width=190,height=50,font=("Bahnschrift SemiBold SemiConden",24))
        self.duration.place(x=5, y = 35)


        # ======================================== BOTTOM BOX ================================================#

        bottombox = CTkLabel(self,height=143, width=1185,text="",bg_color="grey10")
        bottombox.place(x=85, y = 565)

        self.videobox = CTkCanvas(self, width=1920, height=1080)
        self.videobox.place(x=170,y=20) 

        #========================================= VIDEO SECTION =======================================================#

        # video_canvas = CTkCanvas(self,w)

        self.photo = None
        self.stopped = False
        

        playbox = CTkLabel(bottombox, width=390, height=120,bg_color='transparent',text='')
        playbox.place(x=12,y=12)

        textbox = CTkLabel(playbox, text_color='white',font=("Bahnschrift SemiBold SemiConden",14),text="Video Control",bg_color='transparent',)
        textbox.place(x=160,y=1)

        input = CTkLabel(bottombox, width=390, height=120,bg_color='transparent',text='')
        input.place(x=410,y=12)

        inputtextbox = CTkLabel(input, text_color='white',font=("Bahnschrift SemiBold SemiConden",14),text="Video Source",bg_color='transparent',)
        inputtextbox.place(x=160,y=1)

        self.file_name = CTkLabel(input, text_color='white',font=("Bahnschrift SemiBold SemiConden",14),text=f"path : ",bg_color='transparent',)
        self.file_name.place(x=100,y=30)

        self.checkbox_var = BooleanVar()
        self.checkbox1 = CTkCheckBox(input, text="File Source", variable=self.checkbox_var, command=self.on_checkbox_change,font=("Bahnschrift SemiBold SemiConden",14))
        self.checkbox1.place(x=265,y=35)
        
        
        self.manual_input = CTkTextbox(input,height=12,width=200,font=("Bahnschrift SemiBold SemiConden",14))
        self.manual_input.place(x=10 ,y= 65)
        self.manual_input.configure(state="disabled")

        self.checkbox_var_manual = BooleanVar()
        self.checkbox2 = CTkCheckBox(input, text="Manual Source", variable=self.checkbox_var_manual, command=self.on_checkbox_change,font=("Bahnschrift SemiBold SemiConden",14))
        self.checkbox2.place(x=265,y=70)


        self.file_input = CTkButton(input, 
                                 text='Select File',
                                 command=(self.select_file),
                                 fg_color='grey30',
                                 hover_color="#fce101",
                                 width=80,
                                 height=20,
                                 font=("Bahnschrift SemiBold SemiConden",14)
                                
                                 )
        self.file_input.place(x=10, y=35)
        self.file_input.configure(state="disabled")

        play_logo = os.path.join(os.path.dirname(__file__), 'app_asset\play.png')
        imagelogo = CTkImage(light_image=Image.open(play_logo), size=(45,45))
        start_button = CTkButton(playbox, 
                                 text='START DETECTION',
                                 command=(self.start_detection_thread),
                                 fg_color='grey30',
                                 hover_color="#228B22",
                                 width=180,
                                 height=75,
                                 image=imagelogo,
                                 font=("Bahnschrift SemiBold SemiConden",14)
                                 )
        start_button.place(x=10, y=35)

        stop_logo = os.path.join(os.path.dirname(__file__), 'app_asset\stop2.png')
        imagestop = CTkImage(light_image=Image.open(stop_logo), size=(45,45))
        stop_button = CTkButton(playbox, 
                                 text='STOP DETECTION',
                                 command=self.stop_detection,
                                 fg_color='grey30',
                                 hover_color="#FF0000",
                                 width=180,
                                 height=75,
                                 image=imagestop,
                                 font=("Bahnschrift SemiBold SemiConden",14)
                                 )
        stop_button.place(x=200, y=35)

        self.data = {}

        # Untuk File handler csv

        select_folder = CTkLabel(bottombox, width=360, height=120,bg_color='transparent',text='')
        select_folder.place(x=810,y=12)

        select_foldertextbox = CTkLabel(select_folder, text_color='white',font=("Bahnschrift SemiBold SemiConden",14),text="Save Data",bg_color='transparent',)
        select_foldertextbox.place(x=155,y=1)

        self.folderinput = CTkButton(select_folder, 
                                 text='Select Folder',
                                 command=self.select_folder,
                                 fg_color='grey30',
                                 hover_color="#fce101",
                                 width=80,
                                 height=20,
                                 font=("Bahnschrift SemiBold SemiConden",14)
                                
                                 )
        self.folderinput.place(x=10, y=35)
        self.file_input.configure(state="disabled")

        self.folder_name = CTkLabel(select_folder, text_color='white',font=("Bahnschrift SemiBold SemiConden",14),text=f"path : ",bg_color='transparent',)
        self.folder_name.place(x=100,y=30)

        self.checkbox_var_save = BooleanVar()
        self.save = CTkCheckBox(select_folder, text="Save cropped", variable=self.checkbox_var_save,font=("Bahnschrift SemiBold SemiConden",14))
        self.save.place(x=235,y=34)

        self.folder_file_name = CTkEntry(select_folder,height=24,width=250,font=("Bahnschrift SemiBold SemiConden",14),
                                         placeholder_text="",text_color="white")
        self.folder_file_name.place(x=9 ,y= 87)

        self.nameinputfolder = CTkLabel(select_folder, text_color='white',font=("Bahnschrift SemiBold SemiConden",13),text="Input name for folder and data file",bg_color='transparent',)
        self.nameinputfolder.place(x=10,y=58)

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
            initialdir='/',
            filetypes=filetypes
            )
        
        self.filename_var.set(os.path.basename(self.filename))
        self.file_name.configure(text=f"Path : {self.filename_var.get()}")
        # print(self.filename_var)

    def select_folder(self):

        self.foldername_var = StringVar()

        self.foldername = filedialog.askdirectory(title="Select Folder to Save",
                                                  initialdir='/')
        
        self.foldername_var.set(os.path.basename(self.foldername))
        self.folder_name.configure(text=f"Path : {self.foldername_var.get()}")
        
        
    def crop_image(self,img, id):
        
        x = datetime.datetime.now()

        folder_title = str(self.folder_file_name.get(1.0, "end-1c"))
        main_path = f"{str(self.foldername)}"  
        main_folder = os.path.join(main_path, folder_title)

        if not os.path.exists(main_folder):
            os.makedirs(main_folder)

        file_name = f'{id}_{x.hour}_{x.minute}_{x.second}_{x.microsecond}.png'
        cv2.imwrite(os.path.join(main_folder, file_name), img)
        
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
    

    def start_detection_thread(self):
        detection_thread = threading.Thread(target=self.start_detection)
        detection_thread.start()



    def start_detection(self):

        input_content = self.folder_file_name
        if not input_content.get():
             error_message = "File and Folder name is Empty"
             CTkMessagebox(self,title="Error",message=error_message, height=200,width=400,icon="warning",
                          font=("Bahnschrift SemiBold SemiConden",14))
             
             return
        
        self.on_start()
        
        self.stopped = False
        model = YOLO('custom.pt')
        # cap = cv2.VideoCapture("test2.mp4")

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
            
        my_file = open('coco.txt', "r")
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

            if self.stopped:
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

            

            # Convert the frame to RGB format
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # Convert the NumPy array to a PhotoImage object
            self.photo = ImageTk.PhotoImage(Image.fromarray(rgb_frame))
            # Update the videobox canvas with the new image
            self.videobox.create_image(0, 0, anchor=tk.NW, image=self.photo)

            self.videobox.after(10, update_frame)

           
        
        if not self.stopped:
            threading.Thread(target=update_frame).start()
    
    

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
            df = pd.DataFrame.from_dict(self.data, orient='index')
            csv_filename = os.path.join(str(self.foldername), f'{self.folder_file_name.get()}'+'.csv')
            df.to_csv(csv_filename, index_label='ID')
            success_message = f'Data saved to {csv_filename}'
            CTkMessagebox(self, title="Success", message=success_message, height=200, width=400, icon="info",
                        font=("Bahnschrift SemiBold SemiConden", 14))
            



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
    
    run_all_functions()
    app.mainloop()

