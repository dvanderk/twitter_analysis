# Returns the name of the happiest US state based on the sentiments of the tweets in that state
# Called from the command line: python happiest_state.py <sentiment_file> <tweet_file>
# The AFINN-111.txt contains a list of pre-computed sentiments (From University of Washington's Data Manipulation at Scale course on Coursera 

import json
import types
import sys

def main():
    
    words = open(sys.argv[1])
    tweets = open(sys.argv[2])

    word_scores = {} #dictionary of each words's sentiment score
    states = []
    state_score = {} #dictionary of each state's aggregated tweet scores

    #determine each words's sentiment score
    for line in words:
	term, score = line.split("\t")
	word_scores[term] = int(score)

    for line in tweets:
	tweet_dict = json.loads(line)
 	if 'text' in tweet_dict:
            text = tweet_dict['text'].lower() #set all words to lowercase just our sentiment dictionary
            text.encode('utf-8') #remove unicode

        #determine the sentiment for each word, then add them to determine tweet's overall sentiment
	    for word in text.split():
                sentiment = 0
                if word in word_scores:
		    sentiment += word_scores[word]

	if 'place' in tweet_dict and type(tweet_dict['place']) is not types.NoneType:
	    if 'full_name' in tweet_dict['place'] and type(tweet_dict['place']['full_name']) is not types.NoneType:
		if 'country_code' in tweet_dict['place'] and type(tweet_dict['place']['country']) is not types.NoneType:
		    if tweet_dict['place']['country'] == 'United States':
			geoinfo = tweet_dict['place']['full_name']
			info = geoinfo.split()
			state = info[-1]
			if len(state) == 2:
			   states.append(state)
			   if state not in state_score:
				state_score[state] = sentiment
			   else:
				state_score[state] += sentiment

    #print states
    happiest_state = state_score.keys()[0]
    for state in state_score.keys():
	if state_score[state] >= happiest_state:
	    happiest_state = state_score[state]
    print happiest_state


if __name__ == '__main__':
    main()


    
