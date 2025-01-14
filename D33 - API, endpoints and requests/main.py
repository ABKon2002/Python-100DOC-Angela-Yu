import requests
import datetime as dt
import smtplib
from dotenv import load_dotenv
import os
import time

load_dotenv()

MY_LAT = os.getenv("MY_LAT")
MY_LNG = os.getenv("MY_LNG")
SUNTIME_ENDPOINT = "https://api.sunrise-sunset.org/json"
ISS_ENDPOINT = "http://api.open-notify.org/iss-now.json"


def get_sunrise_sunset():  # Returns true if it is the daytime
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
    }
    response = requests.get(SUNTIME_ENDPOINT, params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = dt.datetime.now().hour
    return sunrise + 5 <= time_now <= sunset + 5

def get_ISS_location():
    response = requests.get(url=ISS_ENDPOINT)
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    return (iss_latitude, iss_longitude)

while True:   # Be careful running this!
    time.sleep(60)
    ISS_loc = get_ISS_location()
    if not get_sunrise_sunset() and MY_LAT - 5 <= ISS_loc[0] <= MY_LAT + 5 and MY_LNG - 5 <= ISS_loc[1] <= MY_LNG + 5:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=os.getenv("MY_EMAIL"), password=os.getenv("MY_PASSWORD"))
            connection.sendmail(
                from_addr=os.getenv("MY_EMAIL"),
                to_addrs=os.getenv("RECIPIENT_EMAIL"),
                msg="Subject: Look Up!\n\nThe ISS is above you in the sky and it is night time, so you can easily spot it :)!"
            )
        print("Look up! I sent a mail too :)")
