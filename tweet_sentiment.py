# Derives the overall sentiment of each tweet, equal to the sum of the scores of the sentiment of each word/term in the tweet
# The file AFINN-111.txt contains a list of pre-computed sentiment scores (from the University of Washington's Data Manipulation at Scale course on Coursera)
# Can be run from the command line: python tweet_sentiment.py AFINN-111.txt <twitter file> 

import sys, os
import json


def main():
    words = open(sys.argv[1])
    tweets = open(sys.argv[2])

    #get the sentment score for each word defined in AFINN-111.txt and store in a dictionary
    scores = {}
    for line in words:
	term, score = line.split("\t")
        scores[term] = int(score)


    #sentimentfile = open(os.path.basename(sys.argv[2]))
    tweet_text = []
    for line in tweets:
	tweet_dict = json.loads(line)
	
	if 'text' in tweet_dict:	
	    text = tweet_dict['text'].lower() #set all words to lowercase just our sentiment dictionary
	    tweet_text.append(text.encode('utf-8')) #remove unicode
	
	#determine the sentiment for each word, then add them to determine tweet's overall sentiment
	for tweet in tweet_text:
	    sentiment = 0
	    words = tweet.split()
	    
  	    for word in words:
		if scores.has_key(word):
		    sentiment = sentiment + scores[word]
	    #print each tweets sentiment on a new line
	    print sentiment

if __name__ == '__main__':
    main()
