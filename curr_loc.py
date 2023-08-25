import json
from urllib.request import urlopen
import datetime

def coordinates():
    url = 'http://ipinfo.io/json'
    response = urlopen(url)
    data = json.load(response)
    loc = data['loc']
    
    latitude, longitude = map(float, loc.split(',')) 
    return latitude, longitude

def time_stamp ():
    x = datetime.datetime.now()

    day = x.strftime("%A")
    date = f'{x.day},{x.month},{x.year}'
    hour = f'{x.hour}:{x.minute}:{x.second}'

    return day,date,hour 


'''

if __name__ == '__main__':
    time_stamp()

'''