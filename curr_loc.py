import json
from urllib.request import urlopen
import geocoder as geo
import datetime
import os
import requests
# from dotenv import load_dotenv

def coordinates():
    location = geo.ip('me')
    latitude = location.latlng[0]
    longitude = location.latlng[1]

    return latitude, longitude



# def weather_handle (lat,lon):
#     load_dotenv()
#     API_key = "873520d2e45976e64f92a6b5b0782484"#os.getenv("OPENWEATHER_API_KEY")
#     url = f'http://api.openweathermap.org/geo/1.0/reverse?lat={lat}&lon={lon}&appid={API_key}'
#     response = requests.get(url)
#     print(response)

    
#     # data = response.json()
#     # temp = data['main']['temp']
#     # humid = data['main']['humidity']

#     # print(f'Suhu: {temp}°C')
#     # print(f'Kelembaban: {humid}%')
#     #     #print(f'Kondisi Cuaca: {weather_description}'
    

def time_stamp ():
    x = datetime.datetime.now()

    day = x.strftime("%A")
    date = f'{x.day},{x.month},{x.year}'
    hour = f'{x.hour}:{x.minute}:{x.second}'

    return day,date,hour 




if __name__ == '__main__':
#     #time_stamp()
#     coordinates()
    latitude, longitude = -6.9222,107.6069
    
