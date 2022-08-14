import requests

city=input("En que ciudad queres saber el tiempo?: ")

url="https://api.openweathermap.org/data/2.5/forecast?q={}&appid=c747152e7fd10709c02279830b6afd3a&units=metric".format(city)

res=requests.get(url)

data=res.json()


temp=data["list"][0]["main"]["temp"]
tempmax=data["list"][0]["main"]["temp_max"]
tempmin=data["list"][0]["main"]["temp_min"]

print(f'La temperatura es: {temp}C, con una minima de {tempmin}C y una maxima de {tempmax}C')
