import cv2
import pandas as pd
from ultralytics import YOLO
from tracker import*
import cvzone
import curr_loc as curr_loc
import os
import datetime
import detect


def detect ():

    model = YOLO('custom.pt')
    cap = cv2.VideoCapture("test2.mp4")
    #cap = cv2.imread('download.jpg')


    my_file = open('coco.txt', "r")
    data = my_file.read()
    class_list = data.split("\n") 
    #print(class_list)

    count=0
    tracker=Tracker()
    lat, long = curr_loc.coordinates()

    day,date, hour = curr_loc.time_stamp() 

    data, counter1 = {},[]
    coord_y_line1, offset = 390, 25
    width, height = {},{}

    def crop_image (img):
        x = datetime.datetime.now()
        date = f'Detect at {x.day}_{x.month}_{x.year}'
        hour = x.hour,x.minute,x.second,x.microsecond

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

            
    while True:    
        ret,frame = cap.read()
        if not ret:
            break

        count += 1
        if count % 3 != 0:
            continue
        frame=cv2.resize(frame,(1020,600))
    
        results = model.predict(frame)
        a = results[0].boxes.data
        px = pd.DataFrame(a).astype("float")
        list = []
    
        for index,row in px.iterrows():

            x1=int(row[0])
            y1=int(row[1])
            x2=int(row[2])
            y2=int(row[3])
            d=int(row[5])
            
            c=class_list[d]
            if 'pothole' in c:
                list.append([x1,y1,x2,y2])
        
            
        bbox_id=tracker.update(list)
        for bbox in bbox_id:
            x3,y3,x4,y4,id=bbox
            cx=int(x3+x4)//2
            cy=int(y3+y4)//2
            cv2.circle(frame,(cx,cy),2,(255,0,255),-1)

            if coord_y_line1 < (cy + offset) and coord_y_line1 > (cy - offset) :
                cv2.rectangle(frame,(x3,y3),(x4,y4),(0,255,0),2)
                cvzone.putTextRect(frame,f'id: {id} {c}',(x3,y3),1,1)
                if counter1.count(id) == 0 :
                        width = round( (x2-x1) * 0.1949152542,2) # predict width
                        height = round((y2-y1) * 0.11392405,2)   # predict height 
                        cv2.putText(frame, f'Width: {width}cm', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                        cv2.putText(frame, f'Height: {height}cm,', (x1, y1 - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                        crop = frame[y3:y4,x3:x4]
                        crop_image(crop)
                        counter1.append(id)
                        data[id] = {
                            'Latitude' : lat,
                            'Longtitude' : long,
                            'Day'  : day,
                            'Date' : date,
                            'Time' : hour,
                            'Width' : width,
                            'height' : height
                            
                        }

                        #backward_scan[id] = (cx,cy)

        cv2.line(frame,(3,coord_y_line1),(1018,coord_y_line1),(0,225,225),2)

        cv2.putText(frame, text= f'Total Pothole = {len(counter1)}', org=(30, 450), 
                    fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=0.7, 
                    color=(0, 255, 0),thickness=1)
        
        cv2.putText(frame, text= 'Screening Line', org=(10, 280), 
                    fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=0.5, 
                    color=(0, 255, 0),thickness=1)
        
        cv2.putText(frame, text= f'Loc = {lat,long}', org=(10, 380), 
                    fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=0.5, 
                    color=(0, 255, 0),thickness=1)

    
        cv2.imshow("Pothole Detector", frame)


        if cv2.waitKey(1)&0xFF==27:
            break
    
    print(data)


    df = pd.DataFrame.from_dict(data, orient='index')
    df.reset_index(inplace=True)
    df.rename(columns={'index': 'id'}, inplace=True)
    df.to_csv(f'{date}.csv', index=True)
    

    cap.release()
    cv2.destroyAllWindows()



if __name__ == '__main__':
    detect()
    
