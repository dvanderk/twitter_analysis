# Prints each term found in the tweets in the given tweet file along with its sentiment
# Uses both pre-determined sentiments from AFINN-111.txt (from University of Washington's Data Manipulation at Scale course on Coursera) as well as deriving the sentiment for terms that are not included using the surrounding terms' sentiments
# Runs from the commands linepython term_sentiment.py AFINN-111.txt <twitter file>

import sys
import json

def main():
	word_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])

	tweet_scores = {} #dictionary of tweets' overal sentiments  
	word_scores = {}
	tweet_text = []
	new_words =[]

	#create dictionary for the words and scores for which we already have a score
	for line in word_file:
		term, score = line.split("\t")
		word_scores[term] = int(score) 

	#create list of tweet
	for line in tweet_file:
		tweet = json.loads(line)
		if u'text' in tweet:
			text = tweet['text'].lower()
			tweet_text.append(text.encode('utf-8'))
	

	#now break down all tweets, find words that have no sentiment, give each tweet a sentiment score
	for tweet in tweet_text:
		sentiment = 0 #initially set sentimnt to zero
		tweet_words = tweet.split()
	
		#add sentiment for words we have a score for initially
		for w in tweet_words:
			if w in word_scores:
				print w
				sentiment += word_scores[w]
                	
					
			#add to the list of new words
			else:
				new_words.append(w)
		tweet_scores[tweet] = sentiment

	#determine sentiment scores for new words
	for new_word in new_words:
		pos = neg = total = 0 #create three new variables, all initally set to zero
		for t in tweet_scores: #evaluate each tweet
			if new_word in t:
				if tweet_scores[t] > 0:
		    			pos += 1
	    			elif tweet_scores[t] < 0:
		    			neg += 1
				total += 1
		print new_word + " " + str(((pos - neg)/total))
	        	
	    
     
    #print out each words and its associated sentiment
    #for w in word_scores:
	#print w + " " + str(word_scores[w])


if __name__ == '__main__':
    main()
