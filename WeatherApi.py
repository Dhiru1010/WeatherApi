import requests
from pprint import pprint as pp

import pandas as pd
import json

dataframe = pd.read_json('C:/Users/91812/Documents/Python/in.json')

data_for_lat_lon=dataframe[['lat','lng']]

i=0

for lt,lng in zip(data_for_lat_lon['lat'],data_for_lat_lon['lng']):
    lat = lt
    lon = lng
    url='https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid=3063f276d9585f62b2ddd51cea380ca2&units=metric'.format(lat,lon)

    res = requests.get(url)

    data = res.json()

    temp = data['main']['temp']
    city = data['name']

    i+=1
    print(i ,'lat' , lat , 'lon' , lon ,'temprature of ' , city  ,' is ' , temp)