![image](https://github.com/user-attachments/assets/04836622-94b3-4d73-ad3c-c83462d5f897)

![Python](https://img.shields.io/badge/powered%20by-Python%203.11-yellow)
![tensorflow](https://img.shields.io/badge/powered%20by-torch%202.0.1-orange)
![matplotlib](https://img.shields.io/badge/powered%20by-matplotlib%203.7.2-violet)
![customtkinter](https://img.shields.io/badge/powered%20by-customtkinter%205.2.0-lightblue)
![opencv](https://img.shields.io/badge/powered%20by-opencv_python%204.8.0.76-lightgreen)
![geocoder](https://img.shields.io/badge/powered%20by-geocoder%201.38.1-lightpink)
#

The Pothole Detector is an application designed to identify road potholes by assigning a unique identifier to each pothole, annotating them with coordinates based on their IP address, recording the timestamp of detection, and capturing photographs of each detected pothole. This program is implemented using Python, OpenCV, and YOLOv8.
## History 📚✨
While driving on the highway, I observed road repair workers inspecting potholes. I noticed that their working method seemed less efficient as, for each pothole they encountered, they had to stop their vehicle, capture photographs, and document various details. Perhaps with the existence of this application, it could streamline their work.
## How to try this program 
Clone this repository

    git clone https://github.com/rahmadyan95/Pothole-Detector.git

Open this folder



Make python virtual environment 

    python -m venv env

Activate your virtual environment

    env\Scripts\activate

Install requirements.txt
    
    pip install -r requirements.txt

run this program

    python detect.py
