import os
import json
import sys

def main():
    tweet_file = open(sys.argv[1])

    words = {} #dictionary to hold terms and their frequencies
    tweet_text = [] #holds the texts of the tweets   

    #seperate just the text of the tweets from erroneous data
    for line in tweet_file:
	#print line
	tweet = json.loads(line)
	print tweet['text']
	if 'text' in tweet:
	    print tweet
	    text = tweet['text'].lower()
	    tweet_text.append(text.encode('utf-8'))
    #print tweet_text

    #create the dictionary for each word, counting as we go
    total = 0    
    for t in tweet_text:
	for word in t:
	    if word not in words:
		words[word] = 1
	    else:
		words[word] += 1
	total += 1

    #print out the terms and their frequencies
    for term in words:
	print term + " " + str(words[term]/total)

   # print total
    #print words.keys()
   # print "hello world"
   
if __name__ == '__main__':
    main()

	
