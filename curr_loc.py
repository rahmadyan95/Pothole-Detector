import json
from urllib.request import urlopen
import geocoder as geo
import datetime
import os
import requests
import openmeteo_requests
import requests_cache
import pandas as pd
from retry_requests import retry
import threading
# from dotenv import load_dotenv

def coordinates():
    # location = geo.ip('me')
    # latitude = location.latlng[0]
    # longitude = location.latlng[1]

    latitude = -6.9222
    longitude = 107.6069


    return latitude, longitude


def time_stamp ():
    x = datetime.datetime.now()

    day = x.strftime("%A")
    date = f'{x.day},{x.month},{x.year}'
    hour = f'{x.hour}:{x.minute}:{x.second}'

    return day,date,hour 

def temprature_data(lat,long):
  

    # Setup the Open-Meteo API client with cache and retry on error
    cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
    retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
    openmeteo = openmeteo_requests.Client(session = retry_session)

    # Make sure all required weather variables are listed here
    # The order of variables in hourly or daily is important to assign them correctly below
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": long,
        "current": "temperature_2m",
        "hourly": "temperature_2m"
    }
    responses = openmeteo.weather_api(url, params=params)

    # Process first location. Add a for-loop for multiple locations or weather models
    response = responses[0]
    # print(f"Coordinates {response.Latitude()}°E {response.Longitude()}°N")
    # print(f"Elevation {response.Elevation()} m asl")

    elevation = response.Elevation()


    current = response.Current()
    current_temperature_2m = current.Variables(0).Value()

    # print(f"Current time {current.Time()}")
    # print(f"Current temperature_2m {current_temperature_2m}")

    return current_temperature_2m,elevation

def run_all_functions():
    coordinates_thread = threading.Thread(target=coordinates)
    time_stamp_thread = threading.Thread(target=time_stamp)
    temperature_data_thread = threading.Thread(target=temprature_data, args=coordinates())

    coordinates_thread.start()
    time_stamp_thread.start()
    temperature_data_thread.start()

    coordinates_thread.join()
    time_stamp_thread.join()
    temperature_data_thread.join()

if __name__ == "__main__":
    run_all_functions()





    
