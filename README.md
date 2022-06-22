# Kai
Kai automatically splits a big text into multiple chunks with exactly 256 characters, automatically numbering them with your layout choice, and then tweets them into a thread

# Layout
The layout configuration consists of 4 files, all of them optional:
- firstpre: What will be on the first tweet only, at the start. Usually a title or just left empty.
- thpre: What will be at the start of each tweet of the thread. Usually a "...".
- thpost: What will be on the end of each tweet. Usually a "..." and a number, such as "2/4" indicating what tweet you're on and until what tweet the thread goes.
- lastpost: Optionally finish the thread with something different from thpost. If deleted, thpost will be used.
As an alternative, you could delete all layout config files to just split and tweet the text with no thread numbering or anything.

Kai uses she/her pronouns
