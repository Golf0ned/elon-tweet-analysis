"""
main.py

Conducts sentiment analysis on Elon tweet to give stock recommendations
"""
from time import sleep

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

from twitter import Twitter


def process(body):
    # Create a SentimentIntensityAnalyzer object
    sia = SentimentIntensityAnalyzer()
    sentiment_scores = sia.polarity_scores(body)
    print(sentiment_scores)


def main():
    # Initialize client
    twitter = Twitter()
    twitter.login()

    # start polling most reecnt tweets
    """while(True):
        tweets = twitter.get_tweets('@elonmusk')
        for tweet in tweets:
            sentiment = process(tweet)
        sleep(300)"""
    tweets = twitter.get_tweets()
    for tweet in tweets:
        print(tweet.text)

if __name__=="__main__": 
    main()