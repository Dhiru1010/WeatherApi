import pandas as pd
import json

dataframe = pd.read_json('C:/Users/91812/Documents/Python/WeatherApi/in.json')

Data = []
for i in range(7):
    Data.append(1+i)

Data_Set = pd.DataFrame(Data)
Data_Set.head(5)