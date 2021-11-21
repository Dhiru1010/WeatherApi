import requests
from pprint import pprint as pp

import pandas as pd
import json


dataframe = pd.read_json('C:/Users/91812/Documents/Python/WeatherApi/in.json')

#from json file only use the latitude and longtitude
data_for_lat_lon=dataframe[['lat','lng']]

#take a data name list and store the temp in it
DataSet=['City','latitude','long', 'Weather']
Data=[]

for lt,lng in zip(data_for_lat_lon['lat'],data_for_lat_lon['lng']):
    lat = lt
    lon = lng
    url='https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid=3063f276d9585f62b2ddd51cea380ca2&units=metric'.format(lat,lon)

    data = requests.get(url).json()
    #data gives the the data from the api in form of the json

    temp = data['main']['temp']
    city = data['name']
    #use only specifies data from the json data
    Data.append([city,lat,lon,temp])
    
Data_Set = pd.DataFrame(Data)
Data_Set.columns=['City','latitude','longtitude','Temprature']
Data_Set.dropna(axis = 0, how ='any', inplace=True)
Data_Set.index = pd.RangeIndex(len(Data_Set.index))

Data_Set.to_csv('weatherdata.csv',index=False)
dfs=pd.read_csv('weatherdata.csv')
dfs.head()