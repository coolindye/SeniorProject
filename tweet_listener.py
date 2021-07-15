#imports 
from tweepy import Stream, OAuthHandler
from tweepy.streaming import StreamListener
from progressbar import ProgressBar, Percentage, Bar
import json
import sys

# Authentication Keys
consumerKey = "BOD5rEk4EhxVURpXBVREOIWdZ"
consumerSecret = "LH3Kx96HRC5mevEOoTCIqiuanNjR3OrHj1ZTH15845ao8rNt28"
accessToken = "3309347388-65x6LwVcWcS50jafGLM1Kue4As1A6neudkD64Tk"
accessTokenSecret = "pwHEDyLd5PFbVoxc0uWlS9idTgcGKkc6sTUfctGuOI1UN"

#The number of tweets we want to get
max_tweets = 100

#Create the listener class that receives and saves tweets


class listener(StreamListener):
    #On init, set the counter to zero and create a progress bar
    def __init__(self, api=None):
        self.num_tweets = 0
        self.pbar = ProgressBar(
            widgets=[Percentage(), Bar()], maxval=max_tweets).start()

    #When data is received, do this
    def on_data(self, data):
        #Append the tweet to the 'tweets.txt' file
        with open('tweet_receive.txt', 'a') as tweet_file:
            tweet_file.write(data)
            #Increment the number of tweets
            self.num_tweets += 1
            #Check to see if we have hit max_tweets and exit if so
            if self.num_tweets >= max_tweets:
               self.pbar.finish()
               sys.exit(0)
            else:
                #increment the progress bar
               self.pbar.update(self.num_tweets)
        return True

    #Handle any errors that may occur
    def on_error(self, status):
        print(status)


#Get the OAuth token
auth = OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
#Use the listener class for stream processing
twitterStream = Stream(auth, listener())
#Filter for these topics
twitterStream.filter(track=["obama", "trump", "democrats"])
