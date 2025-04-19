##############################################################################################
## INCOMPLETE CODE: API KEY IS NOT ACTIVATED!
##############################################################################################

import requests

MY_LAT = 17.417509
MY_LONG = 78.368187
MY_API_KEY = '13671566e9cf4f7cdde07e88477b18b1'
API_ENDPOINT =  f'https://api.openweathermap.org/data/2.5/forecast?lat={MY_LAT}&lon={MY_LONG}&appid={MY_API_KEY}'

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": MY_API_KEY
}

weather_data = requests.get(API_ENDPOINT)
weather_data.raise_for_status()
weather_json = weather_data.json()
print(weather_json)