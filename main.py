"""
main.py

Conducts sentiment analysis on Elon tweet to give stock recommendations
"""
import time

from analyze import Analyzer
from twitter import Twitter


def main():
    # initialize client
    twitter = Twitter()
    twitter.login()

    # initialize analyzer
    analyzer = Analyzer()

    # poll every 5 min
    while(True):
        tweets = twitter.get_tweets()
        for tweet in tweets:
            # clean the data
            tweetClean = analyzer.clean(tweet.text)
            # get companies
            companies = analyzer.getCompanies(tweetClean)
            
            # if there are companies, do sentiment analysis (python slow moment)
            sentiment = analyzer.process(tweetClean) if companies else 0
            
            # TODO: do something with the daa lmaao

        time.sleep(300)

if __name__=="__main__": 
    main()