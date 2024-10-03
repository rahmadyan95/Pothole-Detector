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
![01](https://github.com/user-attachments/assets/e81bc3d8-d375-446b-9970-dca47c801314)

### 📷 Detect Road Potholes
First is to detect road potholes using only a regular webcam with OpenCV Python technology and the application of artificial intelligence in object classification to accurately identify potholes.

![image](https://github.com/user-attachments/assets/a0b8ea28-895a-47f1-a054-bd851b6d81b1)


### 🗺️ Show Map
Show map feature is used to display the locations of potholes detected by the camera. The system will record each pothole detected by the camera, and these locations will be displayed on a map using Geocoder and OpenStreetMap.

![06](https://github.com/user-attachments/assets/3f89c11e-d191-4e5a-aa8f-7418f68b29a3)

Not only does it show the location, but the system can also display details based on the ID and show images of the pothole.

![08](https://github.com/user-attachments/assets/8d31ce3c-0bd5-4137-928a-6028d36d09ff) 

![09](https://github.com/user-attachments/assets/46147b42-4b72-4340-bc37-0abe740b27da)


### 📃 Show Data
Show data feature is designed to generate data in PDF format. The report, which is usually created manually by the user, no longer needs to be typed manually. It will automatically appear as a report ready to be signed by the supervisor.

![07](https://github.com/user-attachments/assets/0085ce49-21e7-40f3-b5a6-856a72bee3ae)

Under development
![image](https://github.com/user-attachments/assets/a8ed466c-467f-47e6-813d-986a13a63ef1)

## How To Use 

### Detection Feature

![image](https://github.com/user-attachments/assets/53977618-ea0b-4277-9256-86a66c1b61c1)

<ol>
  <li>Step 1
    <ul>
      <li>Input the video to be detected. This is possible with two inputs: either from a video file in the folder or directly via camera input.</li>
    </ul>
  </li>
  <li>Step 2
    <ul>
      <li>Select the folder to save the detection results in the directory. The file format will be CSV for data. Check the "Save Crop" option to save images of the potholes.</li>
    </ul>
  </li>
  <li>Step 3
    <ul>
      <li>Press the "Start" button to begin detection.</li>
    </ul>
  </li>
  <li>Step 4
    <ul>
      <li>Press the "Stop" button to halt detection.</li>
    </ul>
  </li>
</ol>

### Show Data Feature

![image](https://github.com/user-attachments/assets/837b8e54-5bcb-45ab-ab4c-ac190d99e90f)


<ol>
  <li>Step 1
    <ul>
      <li>Input the data.</li>
    </ul>
  </li>
  <li>Step 2
    <ul>
      <li>Press the "Start" button.</li>
    </ul>
  </li>
  <li>Step 3
    <ul>
      <li>Select the desired chart operation such as:
        <ol type="a">
          <li>ID WIDTH LENGTH DATA</li>
          <li>ID TEMP ELEV DATA</li>
          <li>TIME ELEVATION TEMP DATA</li>
        </ol>
      </li>
    </ul>
  </li>
  <li>Step 4
    <ul>
      <li>Input the necessary data to generate the PDF report.</li>
    </ul>
  </li>
  <li>Step 5
    <ul>
      <li>Press the "Save PDF" button to Save Auto Report PDF.</li>
    </ul>
  </li>

  <li>Step 6
    <ul>
      <li>Press the "Stop" button to complete the process.</li>
    </ul>
  </li>
</ol>

## Licence
 MIT License

    Copyright (c) Microsoft Corporation. All rights reserved.

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE






