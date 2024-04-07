"""
main.py

Conducts sentiment analysis on Elon tweet to give stock recommendations
"""
import json
import os
import time

import dotenv
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

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

    # initialize firebase connection
    dotenv_file = dotenv.find_dotenv()
    dotenv.load_dotenv(dotenv_file)
    FIREBASE_KEY = os.getenv("FIREBASE_KEY")
    cred = credentials.Certificate(json.loads(FIREBASE_KEY))
    app = firebase_admin.initialize_app(cred, {
	'databaseURL':"https://elon-tweet-analysis-default-rtdb.firebaseio.com"
	})
    ref = db.reference('/')


    print('Ready to blast tweets!')
    print('------------------------------\n')

    # poll every 5 min
    while(True):
        # get the tweets
        print('Getting tweets...')
        tweets = twitter.get_tweets(40)

        data = {}
        for index, tweet in enumerate(tweets):
            # clean the data
            tweetClean = analyzer.clean(tweet.text)
            print(tweetClean)
            # get companies
            companies = analyzer.get_companies(tweetClean)
            
            # do sentiment analysis if there are companies or set sentiment to 0 (python slow moment)
            sentiment = analyzer.process(tweetClean) if companies else 0
            print(f'Sentiment: {sentiment}\n\n')

            # insert into json
            cur = { 'tweet' : tweet.text, 
                    'sentiment' : sentiment,
                    'companies' : list(companies), 
                    'index' : index}
            data[index] = cur
            
        # push the json to firebase
        ref.set(data)

        time.sleep(300)

if __name__=="__main__": 
    main()