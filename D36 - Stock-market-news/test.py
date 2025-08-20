import openai
import os
from dotenv import load_dotenv
import requests
from newsapi import NewsApiClient

# Load environment variables from .env file
# The .env file should contain:
#    OPEN_AI_API_KEY=<your_openai_api_key>
#    NEWS_API_KEY=<your_news_api_key>
load_dotenv()

# Initialize News API client
news_api = NewsApiClient(api_key = os.getenv("NEWS_API_KEY"))

def open_ai_test_bot(prompt):
    client = openai.OpenAI(api_key= os.getenv("OPEN_AI_API_KEY"))

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

def llm_test_bot(prompt):
    response = requests.post(
        "https://llmfoundry.straive.com/openai/v1/chat/completions",
        headers={"Authorization": f"Bearer {os.environ['LLMFOUNDRY_TOKEN']}:my-test-project"},
        json={"model": "gpt-4o-mini", "messages": [{"role": "user", "content": prompt}]}
    )
    return response.json()['choices'][0]['message']['content'].strip()

def get_news():
    relevant_articles = news_api.get_everything(q='Indian stock market',
                                      from_param='2025-08-14',
                                      language='en',
                                      sort_by='relevancy')
    if relevant_articles['status'] == 'ok':
        total_articles = relevant_articles['totalResults']
        if total_articles > 0:
            articles = relevant_articles['articles']
            news_summary = []
            for article in articles[:5]:
                title = article['title']
                description = article['description']
                url = article['url']
                news_summary.append(f"Title: {title}\nDescription: {description}\nURL: {url}\n")
            return total_articles, "\n".join(news_summary)
        else:
            return "No relevant articles found."
    else:
        return "Error fetching news articles."

if __name__ == "__main__":

    N, news_summary = get_news()
    if isinstance(N, int):
        print(f"Total relevant articles found: {N}")
        print("News Summary:")
        print(news_summary)

    # while True:
    #     prompt = input("You: ")
    #     # For testing purposes, you can hardcode a prompt
    #     # prompt = "What is the weather like in Kottayam, Kerala today? Would you advise an umbrella?"
    #     if prompt.lower() in ["exit", "quit", "stop"]:
    #         print("Exiting the chat.")
    #         break
        
    #     # prompt = "What is the weather like in New York City today?"
    #     response = llm_test_bot(prompt)
    #     print(f'\nZen: {response}\n')