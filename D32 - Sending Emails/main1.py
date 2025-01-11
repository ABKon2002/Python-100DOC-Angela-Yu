import smtplib
import datetime as dt
import os
from dotenv import load_dotenv
from random import randint

load_dotenv()

with open("D32 - Sending Emails\\quotes.txt") as quote_file:
    quotes = quote_file.read().split("\n")
    quote = quotes[randint(0, len(quotes) - 1)].strip()
    if dt.datetime.now().weekday() == 5:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user = os.getenv('MY_EMAIL'), password = os.getenv('MY_PASSWORD'))
            content = f"Subject:Motivating you in ChristCode!\n\n{quote}\nMay God bless you!"
            connection.sendmail(
                from_addr = os.getenv('MY_EMAIL'),
                to_addrs = os.getenv('RECIPIENT_EMAIL'),
                msg = content
            )
        print(f"Email sent with the quote: {quote}! ")
