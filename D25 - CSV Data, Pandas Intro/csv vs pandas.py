
# import csv

# with open('D25 - CSV Data, Pandas Intro/Data/weather_data.csv') as data:
#     reader = csv.reader(data)
#     temperatures = []
#     for row in reader:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

import numpy as np
import pandas as pd

data = pd.read_csv('D25 - CSV Data, Pandas Intro/Data/weather_data.csv')
print(round(data['temp'].mean(), 2))

max_temp_day = data[data.temp == data['temp'].max()]
print(type(max_temp_day))
print(max_temp_day)

monday = data[data.day == 'Monday']
print((monday.temp[0] * (9/5)) + 32, 'fahrenheit')

data_dict = {
    'Students' : ['Amy', 'Jake', 'Scully'],
    'Marks' : [23, 21, 23]
}

dataFrame = pd.DataFrame(data_dict)
print(dataFrame)
dataFrame.to_csv('D25 - CSV Data, Pandas Intro/Data/test_data.csv')
