import tweepy
import os

consumer_key = open("config/apikey", "r").read().replace('\n','')
consumer_secret = open("config/apisecret", "r").read().replace('\n','')
access_token = open("config/apitoken", "r").read().replace('\n','')
access_token_secret = open("config/tokensecret", "r").read().replace('\n','')


print(consumer_key)

#login
client = tweepy.Client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret
)






tweet =  client.create_tweet(text="hello")
tweet2 = client.create_tweet(text="hi", in_reply_to_tweet_id=tweet.data["id"])
