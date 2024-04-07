"""
main.py

Conducts sentiment analysis on Elon tweet to give stock recommendations
"""
import time

from analyze import Analyzer
from twitter import Twitter


def main():
    # initialize client
    print('Logging into twitter...')
    twitter = Twitter()
    twitter.login()
    print('Done!')

    # initialize analyzer
    print('Initializing analyzer...')
    analyzer = Analyzer()
    print('Done!')

    print('Ready to blast tweets!')
    print('------------------------------\n')

    # poll every 5 min
    while(True):
        print('Getting tweets...')
        tweets = twitter.get_tweets()
        for tweet in tweets:
            # clean the data
            tweetClean = analyzer.clean(tweet.text)
            print(tweetClean)
            # get companies
            companies = analyzer.get_companies(tweetClean)
            
            # if there are companies, do sentiment analysis (python slow moment)
            sentiment = analyzer.process(tweetClean) if companies else 0
            print(f'Sentiment: {sentiment}\n\n')
            

        time.sleep(300)

if __name__=="__main__": 
    main()