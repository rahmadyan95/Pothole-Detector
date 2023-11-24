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

        self.detection_running = False
        
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
        
        lat, long = curr_loc.coordinates()

        sidebox = CTkLabel(self,height=542, width=210,text="",bg_color="grey10")
        sidebox.place(x=1060, y = 10)

        latitude = CTkLabel(sidebox,text=f'Latitude = {lat}\nLongitude = {long}',bg_color="grey10",font=("consolas",12),text_color='white')
        latitude.place(x=10, y = 10)
        



        # ======================================== BOTTOM BOX ================================================#

        bottombox = CTkLabel(self,height=143, width=1185,text="",bg_color="grey10")
        bottombox.place(x=85, y = 565)

        #========================================= VIDEO SECTION =======================================================#

        # video_canvas = CTkCanvas(self,w)

        self.videobox = CTkCanvas(self, width=1920, height=1080)
        self.videobox.place(x=170,y=20) 

        self.photo = None

        play_logo = os.path.join(os.path.dirname(__file__), 'app_asset\play.png')
        imagelogo = CTkImage(light_image=Image.open(play_logo), size=(45,45))

        playbox = CTkLabel(bottombox, width=390, height=120,bg_color='transparent',text='')
        playbox.place(x=12,y=12)

        textbox = CTkLabel(playbox, text_color='white',font=("Bahnschrift SemiBold SemiConden",14),text="Video Contol",bg_color='transparent',)
        textbox.place(x=160,y=1)

        start_button = CTkButton(playbox, 
                                 text='START DETECTION',
                                 command=self.start_detection,
                                 fg_color='grey30',
                                 hover_color="#228B22",
                                 width=180,
                                 height=75,
                                 image=imagelogo,
                                 font=("Bahnschrift SemiBold SemiConden",14)
                                 )
        start_button.place(x=10, y=35)

        stop_button = CTkButton(playbox, 
                                 text='STOP DETECTION',
                                 command=self.start_detection,
                                 fg_color='grey30',
                                 hover_color="#FF0000",
                                 width=180,
                                 height=75,
                                 image=imagelogo,
                                 font=("Bahnschrift SemiBold SemiConden",14)
                                 )
        stop_button.place(x=200, y=35)
         

        


        
    def start_detection(self):
        model = YOLO('custom.pt')
        cap = cv2.VideoCapture("test2.mp4")

        my_file = open('coco.txt', "r")
        data = my_file.read()
        class_list = data.split("\n")

        count = 0
        tracker = Tracker()
        # lat, long = curr_loc.coordinates()

        day, date, hour = curr_loc.time_stamp()
        lat, long = curr_loc.coordinates()

        data, counter1 = {}, []
        coord_y_line1, offset = 700, 40
        width, height = {}, {}

        def crop_image(img, id):
            x = datetime.datetime.now()
            date = f'Detect at {x.day}_{x.month}_{x.year}'
            hour = x.hour, x.minute, x.second, x.microsecond

            fol_nam = "cropped_photo"
            dir_path = date

            fol_path = os.path.join(fol_nam, dir_path)

            if os.path.exists(fol_path) and os.path.isdir(fol_path):
                pass
            else:
                os.makedirs(fol_path)

            # saving file
            file_name = f'{id}_{hour}.png'
            cv2.imwrite(os.path.join(fol_path, file_name), img)

        def update_frame():
            nonlocal count
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
                        width = round((x2 - x1) * 0.1949152542, 2)  # predict width
                        height = round((y2 - y1) * 0.11392405, 2)  # predict height
                        cv2.putText(frame, f'Width: {width}cm', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                    (0, 0, 255), 2)
                        cv2.putText(frame, f'Height: {height}cm,', (x1, y1 - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                    (0, 0, 255), 2)
                        crop = frame[y3:y4, x3:x4]
                        crop_image(crop, id)
                        counter1.append(id)
                        data[id] = {
                            'Latitude': lat,
                            'Longtitude': long,
                            'Day': day,
                            'Date': date,
                            'Time': hour,
                            'Width': width,
                            'height': height
                        }

            cv2.line(frame, (3, coord_y_line1), (1920, coord_y_line1), (0, 225, 225), 5)

            cv2.putText(frame, text=f'Total Pothole = {len(counter1)}', org=(30, 450),
                        fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=0.7,
                        color=(0, 255, 0), thickness=1)

            cv2.putText(frame, text='Screening Line', org=(10, 600),
                        fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=1,
                        color=(0, 255, 0), thickness=2)

            cv2.putText(frame, text=f'Loc = {lat, long}', org=(10, 380),
                        fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=0.5,
                        color=(0, 255, 0), thickness=1)

            # Convert the frame to RGB format
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # Convert the NumPy array to a PhotoImage object
            self.photo = ImageTk.PhotoImage(Image.fromarray(rgb_frame))
            # Update the videobox canvas with the new image
            self.videobox.create_image(0, 0, anchor=tk.NW, image=self.photo)

            self.videobox.after(10, update_frame)

        update_frame()
    
        # def start_vid():
        #     threading.Thread(target=start_detection,args=()).start()
            
        

        # Add a button to start the detection
        

    
        #======================================== END VIDEO SECTION ===================================================== #
        


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

