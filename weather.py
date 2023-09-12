import requests

city = input("Enter City:")
key = "873520d2e45976e64f92a6b5b0782484"

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric".format(city)

res = requests.get(url)
data = res.json()
# print(data)

humidity = data['main']['humidity']
pressure = data['main']['pressure']
wind = data['wind']['speed']
description = data['weather'][0]['description']
temp = data['main']['temp']

print('Temperature:',temp,'°C')
print('Wind:',wind)
print('Pressure: ',pressure)
print('Humidity: ',humidity)
print('Description:',description)