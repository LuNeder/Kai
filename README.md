# Kai
Kai automatically splits a big text into multiple chunks with exactly 500 characters (for Mastodon) and 280 characters (for Twitter), automatically numbering them with your layout choice, and then toots and tweets them into a mastodon and twitter thread.

# Usage
Write the text you want to toot and/or tweet on the "tweet" file.

# Configuration and Layout
### Layout Files
The layout configuration consists of 4 files, all of them optional:
<!--
- firstpre: What will be on the first tweet only, at the start. Usually a title or just left empty.
-->
- thpre: What will be at the start of each tweet of the thread. Usually a "...".
- thpost: What will be on the end of each tweet. Usually a "..." and a number, such as "2/4" indicating what tweet you're on and until what tweet the thread goes.
- lastpost: Like thpost, but for the last tweet.
As an alternative, you could delete all layout config files to just split and tweet the text with no thread numbering or anything.
### Configuration files
- platform: "m" for Mastodon, "t" for twitter, "mt" for both. If you use some kind of automatic crossposter, it’s recommended to use Kai with only one of the platforms and then let the crossposter do its job.
##### Twitter:
- apikey:
- apisecret:
- apitoken:
- tokensecret:
<!--
- twtuser: 
-->
##### Mastodon:
- mastaccesstoken: 
### Variables
The following variables can be added to the above files and will be automatically changed by Kai.
<!--
- %?: Title
- %u: @username of who's tweeting (defined in configuration files)
-->
- %nu: Number of the current tweet on the thread
  - %n can also be used, but only for threads with less than 100 tweets
- %TO: Total number of tweets on the thread
  - %T can also be used, but only for threads with less than 100 tweets
# Limitations
- A thread with 1000 tweets or more might not come out as expected if using %nu and/or %TO on layout

#
Kai uses she/her pronouns
