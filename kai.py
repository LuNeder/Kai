# Copyright (c) Luana Neder 2022
# Licensed under the Open Software License version 3.0

import tweepy
import os
from textwrap import wrap
from mastodon import Mastodon


tootmaxsize = 500


platforms = open("config/apikey", "r").read().replace('\n','')
if "m" in platforms:
    platform_m = 1
else:
    platform_m = 0
if "t" in platforms:
    platform_t = 1
else:
    platform_t = 0


#login info - twitter
if platform_t == 1:
    consumer_key = open("config/apikey", "r").read().replace('\n','')
    consumer_secret = open("config/apisecret", "r").read().replace('\n','')
    access_token = open("config/apitoken", "r").read().replace('\n','')
    access_token_secret = open("config/tokensecret", "r").read().replace('\n','')

#login info - Mastodon
if platform_m == 1:
    mastodon_access_token = open("config/mastaccesstoken", "r").read().replace('\n','')


#login twitter
if platform_t == 1:
    client = tweepy.Client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret
)

#login Mastodon
if platform_m == 1:
    mastodon = Mastodon(access_token = mastodon_access_token)

################


file = open("tweet", "r").read()
txtsize = len(file)

#get configs
fstpre = open("config/firstpre", "r").read()
fstpresize = len(fstpre)

pre = open("config/thpre", "r").read()
presize = len(pre)

post = open("config/thpost", "r").read()
postsize = len(post)

lastpost = open("config/lastpost", "r").read()
lstpostsize = len(lastpost)


#fstsize = 280 - fstpresize - postsize
#print(fstsize)

tweetsize = 280 - presize - postsize
print(tweetsize)

lastsize = 280 - presize - lstpostsize
print(lastsize)



tootsize = tootmaxsize - presize - postsize
print(tootsize)

mastlastsize = tootmaxsize - presize - lstpostsize
print(mastlastsize)

#fsttweet = wrap(file, fstsize, break_on_hyphens=False) # drop_whitespace=False does not work. how do I allow words to be broken in half?
#print(fsttweet)
#fsttweet = fsttweet[0]
#print(fsttweet)

#divide big text in tweets
tweets = wrap(file, tweetsize, break_on_hyphens=False)
twtnump = len(tweets)
print(tweets)

#divide big text in toots
toots = wrap(file, tootsize, break_on_hyphens=False)
tootnump = len(toots)
print(toots)


########## 

if len(tweets[twtnump - 1]) > lastsize:
	print("last twt will have to be split")
	alasttweets = wrap(tweets[twtnump - 1], lastsize)
	number = twtnump + len(alasttweets) - 1
else:
	print("last twt will not have to be split")
	number = twtnump
	
print("there will be " + str(number) + " tweets")


#twttxt = fstpre + fsttweet + post

for i in range(twtnump):
	if i == 0:
		print("1st tweet now")
		tweeti = tweets[i]
		#twttxt = fstpre + fsttweet + post
		posti = post.replace("%nu", str(i + 1)).replace("%n", str(i + 1)).replace("%TO", str(number)).replace("%T", str(number))
		twttxt = tweeti + posti
		tweet =  client.create_tweet(text=twttxt)
		#print("1st tweet done")
	elif i == len(tweets) - 1:
		print("last tweet now")
		tweeti = tweets[i]
		
		if len(tweeti) > lastsize:
			print("will split last tweet")
			lasttweets = wrap(tweeti, lastsize)
			for f in range(len(lasttweets)):
				if f == len(lasttweets) - 1:
					print("final last twt now")
					tweeti = lasttweets[f]
					prei = pre.replace("%nu", str(i + f + 1)).replace("%n", str(i + f + 1)).replace("%TO", str(number)).replace("%T", str(number))
					lastposti = lastpost.replace("%nu", str(i + f + 1)).replace("%n", str(i + f + 1)).replace("%TO", str(number)).replace("%T", str(number))
					twttxt = prei + tweeti + lastposti
					tweet = client.create_tweet(text=twttxt, in_reply_to_tweet_id=tweet.data["id"])
				else:
					print("lst twt part " + str(f) + "+1 now")
					tweeti = lasttweets[f]
					prei = pre.replace("%nu", str(i + f + 1)).replace("%n", str(i + f + 1)).replace("%TO", str(number)).replace("%T", str(number))
					posti = post.replace("%nu", str(i + f + 1)).replace("%n", str(i + f + 1)).replace("%TO", str(number)).replace("%T", str(number))
					twttxt = prei + tweeti + posti
					tweet = client.create_tweet(text=twttxt, in_reply_to_tweet_id=tweet.data["id"])
		else:
			print("no need to split")
			prei = pre.replace("%nu", str(i + 1)).replace("%n", str(i + 1)).replace("%TO", str(number)).replace("%T", str(number))
			lastposti = lastpost.replace("%nu", str(i + 1)).replace("%n", str(i + 1)).replace("%TO", str(number)).replace("%T", str(number))
			twttxt = prei + tweeti + lastposti
			tweet = client.create_tweet(text=twttxt, in_reply_to_tweet_id=tweet.data["id"])
	else:
		print("tweet " + str(i) + "+1 now")
		tweeti = tweets[i]
		prei = pre.replace("%nu", str(i + 1)).replace("%n", str(i + 1)).replace("%TO", str(number)).replace("%T", str(number))
		posti = post.replace("%nu", str(i + 1)).replace("%n", str(i + 1)).replace("%TO", str(number)).replace("%T", str(number))
		twttxt = prei + tweeti + posti
		tweet = client.create_tweet(text=twttxt, in_reply_to_tweet_id=tweet.data["id"])
		#print("tweet " + str(i) + "+1 done")


#tweet =  client.create_tweet(text="hello")
#tweet2 = client.create_tweet(text="hi", in_reply_to_tweet_id=tweet.data["id"])
