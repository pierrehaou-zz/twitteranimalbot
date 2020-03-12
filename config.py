import tweepy
import twittercredentials
import os


def create_api():
    # authenticating to twitter
    consumer_key = os.environ.get("T1CONSUMER_KEY")
    consumer_secret = os.environ.get("T1CONSUMER_SECRET")
    access_key = os.environ.get("T1ACCESS_KEY")
    access_secret = os.environ.get("T1ACCESS_SECRET")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)

    # Create API object
    # Can use methods from API class to access Twitter API's functionality
    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)

    return api
