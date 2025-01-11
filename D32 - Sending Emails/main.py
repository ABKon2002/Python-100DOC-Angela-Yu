import pandas as pd
import datetime as dt
import random
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

birthdays = pd.read_csv("D32 - Sending Emails\\birthdays.csv")
birthdays_dict = {(row["month"], row["day"]): row for (_, row) in birthdays.iterrows()}

now = dt.datetime.now()
today = (now.month, now.day)
if today in birthdays_dict:
    birthday = birthdays_dict[today]
    letter = random.choice(["letter_1", "letter_2", "letter_3"])
    with open(f"D32 - Sending Emails\\letter_templates\\{letter}.txt") as file:
        contents = file.read()
        contents = contents.replace("[NAME]", birthday["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user = os.getenv('MY_EMAIL'), password = os.getenv('MY_PASSWORD'))
        connection.sendmail(
            from_addr = os.getenv('MY_EMAIL'),
            to_addrs = birthday["email"],
            msg = f"Subject:Happy Birthday!\n\n{contents}"
        )
    print(f"Email sent to {birthday['name']}! ")
