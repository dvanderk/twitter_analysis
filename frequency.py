# Compute the frequency of each word/term in tweets from a file of streamed twitter data
# Runs from the command line: python frequency.py <tweet_file> 
# Written in Python v. 2.7

import os
import json
import sys

def main():
    tweet_file = open(sys.argv[1])
    words = {} #dictionary to hold terms and their frequencies   
    total = 0

    #seperate just the text of the tweets from erroneous data
    for line in tweet_file:
	tweet = json.loads(line)
	if 'text' in tweet:
	    text = tweet['text'].lower().encode('utf-8').split()
	    #create the dictionary for each word, counting as we go
	    for term in text:
		if term in words:
		    words[term] += 1
		else:
		    words[term] = 1
	    total += 1


    #print out the terms and their frequencies
    for term in sorted(words, key = words.get):
	print term ," ", (words[term]/float(total))

   
if __name__ == '__main__':
    main()

	
