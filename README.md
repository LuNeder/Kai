# Kai
Kai automatically splits a big text into multiple chunks with exactly 280 characters, automatically numbering them with your layout choice, and then tweets them into a thread

# Usage

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
- apikey:
- apisecret:
- apitoken:
- tokensecret:
- twtuser: 
### Variables
The following variables can be added to the above files and will be automatically changed by Kai.
- %T: Title
- %u: @username of who's tweeting (defined in configuration files)
- %n: Number of the current tweet on the thread
- %F: Total number of tweets on the thread

#
Kai uses she/her pronouns
