import tweepy
import os

consumer_key = open("config/apikey", "r").read()
consumer_secret = open("config/apisecret", "r").read()
access_token = open("config/apitoken", "r").read()
access_token_secret = open("config/tokensecret", "r").read()


client = tweepy.Client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret
)

tweet =  client.create_tweet(text="test")
tweet2 = client.create_tweet(text="testing", in_reply_to_tweet_id=tweeet.id)
