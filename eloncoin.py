"""
eloncoin.py

Conducts sentiment analysis on Elon tweet to give stock recommendations
"""

import twikit
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from twikit import Client
from dotenv import load_dotenv
import os

# Create a SentimentIntensityAnalyzer object
sia = SentimentIntensityAnalyzer()

def process(body):
    sentiment_scores = sia.polarity_scores(body)
    print(sentiment_scores)

def login(client):
    if os.path.exists(os.path.join(os.getcwd(), "cookies.json")):
        client.load_cookies('cookies.json')
    else:
        load_dotenv()

        USERNAME = os.getenv("USERNAME")
        EMAIL = os.getenv("EMAIL")
        PASSWORD = os.getenv("PASSWORD")

        client.login(
            auth_info_1=USERNAME ,
            auth_info_2=EMAIL,
            password=PASSWORD
        )

        client.save_cookies('cookies.json')

def main():
    # Initialize client
    client = Client('en-US')
    login(client)
    process("Tesla Robotaxi unveil on 8/8")

if __name__=="__main__": 
    main() 