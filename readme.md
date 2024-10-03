![image](https://github.com/user-attachments/assets/04836622-94b3-4d73-ad3c-c83462d5f897)

![Python](https://img.shields.io/badge/powered%20by-Python%203.11-yellow)
![tensorflow](https://img.shields.io/badge/powered%20by-torch%202.0.1-orange)
![matplotlib](https://img.shields.io/badge/powered%20by-matplotlib%203.7.2-violet)
![customtkinter](https://img.shields.io/badge/powered%20by-customtkinter%205.2.0-lightblue)
![opencv](https://img.shields.io/badge/powered%20by-opencv_python%204.8.0.76-lightgreen)
![geocoder](https://img.shields.io/badge/powered%20by-geocoder%201.38.1-lightpink)
#

The Pothole Detector is an application designed to identify road potholes by assigning a unique identifier to each pothole, annotating them with coordinates based on their IP address, recording the timestamp of detection, and capturing photographs of each detected pothole. This program is implemented using Python, OpenCV, and YOLOv8.

While driving on the highway, I observed road repair workers inspecting potholes. I noticed that their working method seemed less efficient as, for each pothole they encountered, they had to stop their vehicle, capture photographs, and document various details. Perhaps with the existence of this application, it could streamline their work.

## Main Feature 
![01](https://github.com/user-attachments/assets/0043aed7-89f9-4010-a377-e9b18b3ea9d6)

First is to detect road potholes using only a regular webcam with OpenCV Python technology and the application of artificial intelligence in object classification to accurately identify potholes.

Show map feature is used to display the locations of potholes detected by the camera. The system will record each pothole detected by the camera, and these locations will be displayed on a map using Geocoder and OpenStreetMap.

Show data feature is designed to generate data in PDF format. The report, which is usually created manually by the user, no longer needs to be typed manually. It will automatically appear as a report ready to be signed by the supervisor.
