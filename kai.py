import tweepy
import os




client = tweepy.Client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret
)

tweet =  client.create_tweet(text="test1uu2a3123")
print(tweet)

tweet2 = client.create_tweet(text="testing", in_reply_to_tweet_id=tweet.data["id"])
