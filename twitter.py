import os

from dotenv import load_dotenv
import twikit
from twikit import Client

ELON = "elonmusk"

class Twitter:

    def __init__(self):
        self.client = Client('en-US')

    def login(self):
        """Login to Twitter"""
        if os.path.exists(os.path.join(os.getcwd(), "cookies.json")):
            # load cookies to login
            self.client.load_cookies('cookies.json')
        else:
            # load login info
            load_dotenv()
            USERNAME = os.getenv("USERNAME")
            EMAIL = os.getenv("EMAIL")
            PASSWORD = os.getenv("PASSWORD")

            # login
            self.client.login(
                auth_info_1=USERNAME,
                auth_info_2=EMAIL,
                password=PASSWORD
            )

            # save cookies to file
            self.client.save_cookies('cookies.json')

    def get_tweets(self):
        cur_user = self.client.get_user_by_screen_name(ELON)
        recent_tweets = self.client.get_user_tweets(user_id=cur_user.id, tweet_type="Tweets", count=20)
        return recent_tweets