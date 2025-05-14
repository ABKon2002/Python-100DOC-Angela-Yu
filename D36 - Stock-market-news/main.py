import requests
import os
from dotenv import load_dotenv

load_dotenv()

INVESTED_FUNDS = ['Nippon India Large Cap Fund - Growth', 'Nippon India Small Cap Fund - Growth', 'Motilal Oswal Midcap Regular Growth']

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

indianURL = "https://stock.indianapi.in/mutual_funds"
headers = {"X-Api-Key": os.getenv("STOCK_API_KEY")}
response = requests.get(indianURL, headers=headers)
data = response.json()

invested_funds_fetch = []

for category, fund_list in data.items():
    for type in fund_list:
        for fund in fund_list[type]:
            if 'fund_name' in fund and fund['fund_name'] in INVESTED_FUNDS:
                invested_funds_fetch.append(fund)

# for fund in nippon_funds:
#     print(fund)

for fund in invested_funds_fetch:
    if abs(fund['percentage_change']) > 0.25:
        print(f"{fund['fund_name']} : {fund['percentage_change']}% is moving!")
        print(f"Get News about {fund['fund_name']}")
#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

