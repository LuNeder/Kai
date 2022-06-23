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

lastpost = open("config/lastpost", "r").read()
lstpostsize = len(lastpost)


#fstsize = 280 - fstpresize - postsize
#print(fstsize)

tweetsize = 280 - presize - postsize
print(tweetsize)

lastsize = 280 - presize - lstpostsize



#fsttweet = wrap(file, fstsize, break_on_hyphens=False) # drop_whitespace=False does not work. how do I allow words to be broken in half?
#print(fsttweet)
#fsttweet = fsttweet[0]
#print(fsttweet)

tweets = wrap(file, tweetsize, break_on_hyphens=False)
twtnump = len(tweets)
print(tweets)


#twttxt = fstpre + fsttweet + post

for i in range(twtnump):
	if i == 0:
		print("1st tweet now")
		tweeti = tweets[i]
		#twttxt = fstpre + fsttweet + post
		twttxt = tweeti + post
		tweet =  client.create_tweet(text=twttxt)
		print("1st tweet done")
	elif i == len(tweets) - 1:
		print("last tweet now")
		tweeti = tweets[i]
		
		if len(tweeti) > lastsize:
			print("will split last tweet")
			lasttweets = wrap(tweeti, lastsize)
			for i in range(len(lasttweets)):
				if i == len(lasttweets) - 1:
					print("final last twt now")
					tweeti = lasttweets[i]
					twttxt = pre + tweeti + lastpost
					tweet = client.create_tweet(text=twttxt, in_reply_to_tweet_id=tweet.data["id"])
				else:
					print("lst twt part" + str(i) + "+1 now")
					tweeti = lasttweets[i]
					twttxt = pre + tweeti + post
					tweet = client.create_tweet(text=twttxt, in_reply_to_tweet_id=tweet.data["id"])
		else:
			print("no need to split")
			twttxt = pre + tweeti + lastpost
			tweet = client.create_tweet(text=twttxt, in_reply_to_tweet_id=tweet.data["id"])
	else:
		print("tweet " + str(i) + "+1 now")
		tweeti = tweets[i]
		twttxt = pre + tweeti + post
		tweet = client.create_tweet(text=twttxt, in_reply_to_tweet_id=tweet.data["id"])
		print("tweet " + str(i) + "+1 done")


#tweet =  client.create_tweet(text="hello")
#tweet2 = client.create_tweet(text="hi", in_reply_to_tweet_id=tweet.data["id"])
