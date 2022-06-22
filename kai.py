import tweepy
import os
from textwrap import wrap

consumer_key = open("config/apikey", "r").read().replace('\n','')
consumer_secret = open("config/apisecret", "r").read().replace('\n','')
access_token = open("config/apitoken", "r").read().replace('\n','')
access_token_secret = open("config/tokensecret", "r").read().replace('\n','')



#login
client = tweepy.Client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret
)



file = open("tweet", "r").read()
txtsize = len(file)

fstpre = open("config/firstpre", "r").read()
fstpresize = len(fstpre)

pre = open("config/thpre", "r").read()
presize = len(pre)

post = open("config/thpost", "r").read()
postsize = len(post)


fstsize = 280 - fstpresize - postsize
print(fstsize)

tweetsize = 280 - presize - postsize
print(tweetsize)



fsttweet = wrap(file, fstsize)
print(fsttweet)
fsttweet = fsttweet[0]
print(fsttweet)



tweet =  client.create_tweet(text="hello")
tweet2 = client.create_tweet(text="hi", in_reply_to_tweet_id=tweet.data["id"])
