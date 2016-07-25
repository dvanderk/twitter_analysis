# Computes ten most frquently occuring hashtags from a json file of twitter data
# Runs from the comnand line: python top_ten.py <tweetfile>

import os
import json
import sys
import types


def main():
    tweets = open(sys.argv[1]) #read in command line argument -- file from twitter stream
    hashtag_freq = {} #hashtags and their frequency    

    for line in tweets:
	tweet = json.loads(line)
	if 'entities' in tweet and type(tweet['entities']) is not types.NoneType:
	    if 'hashtags' in tweet['entities'] and type(tweet['entities']['hashtags']) is not types.NoneType:
		hashtags = tweet['entities']['hashtags'] 
		for hashtag in hashtags:
		    htag = hashtag['text'].encode('utf-8')
		    if htag not in hashtag_freq:
			hashtag_freq[htag] = 1
		    else:
		    	hashtag_freq[htag] += 1

    count = 0
    #sorted(hashtag_freq.items(), key = lambda x: x:x[1], reverse=True)
    while count < 11:
	print sorted(hashtag_freq.items(), key = lambda x:x[1], reverse=True)[count][0],
	print " ",
	print sorted(hashtag_freq.items(), key = lambda x:x[1], reverse=True)[count][1]
	count += 1

if __name__ == '__main__':
    main()
	


