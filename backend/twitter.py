import json
import os

import dotenv
import twikit
from twikit import Client

ELON = "elonmusk"

class Twitter:

    def __init__(self):
        self.client = Client('en-US')

    def login(self):
        """Login to Twitter"""
        dotenv_file = dotenv.find_dotenv()
        dotenv.load_dotenv(dotenv_file)
        COOKIES = os.getenv("COOKIES")
        if COOKIES:
            self.client.set_cookies(json.loads(COOKIES))
        else:
            # load login info
            TWITTERUSERNAME = os.getenv("TWITTERUSERNAME")
            EMAIL = os.getenv("EMAIL")
            TWITTERPASSWORD = os.getenv("TWITTERPASSWORD")
            print(TWITTERUSERNAME, EMAIL, TWITTERPASSWORD)

            # login
            self.client.login(
                auth_info_1=TWITTERUSERNAME,
                auth_info_2=EMAIL,
                password=TWITTERPASSWORD
            )

            # save cookies to .env
            cookies = self.client.get_cookies()
            dotenv.set_key(dotenv_file, "COOKIES", json.dumps(cookies))
        
        # debug logging
        print('logged in!')


    def get_tweets(self):
        cur_user = self.client.get_user_by_screen_name(ELON)
        recent_tweets = self.client.get_user_tweets(user_id=cur_user.id, tweet_type="Tweets", count=20)
        return recent_tweets