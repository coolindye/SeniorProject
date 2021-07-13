# Install Libraris
# !pip install textblob
# !pip install tweepy
import matplotlib.pyplot as plt
import tweepy
import sys
from textblob import TextBlob
# Import Libraries

# Authentication Keys
consumerKey = "BOD5rEk4EhxVURpXBVREOIWdZ"
consumerSecret = "LH3Kx96HRC5mevEOoTCIqiuanNjR3OrHj1ZTH15845ao8rNt28"
accessToken = "3309347388-65x6LwVcWcS50jafGLM1Kue4As1A6neudkD64Tk"
accessTokenSecret = "pwHEDyLd5PFbVoxc0uWlS9idTgcGKkc6sTUfctGuOI1UN"


auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)
#Sentiment Analysis


def percentage(part, whole):
    return 100 * float(part)/float(whole)


keyword = input("Please enter keyword or hashtag to search: ")
noOfTweet = int(input("Please enter how many tweets to analyze: "))

tweets = tweepy.Cursor(api.search, q=keyword).items(noOfTweet)

positive = 0
negative = 0
neutral = 0
polarity = 0

for tweet in tweets:
    #print(tweet.text)
    analysis = TextBlob(tweet.text)
    polarity += analysis.sentiment.polarity

    if (analysis.sentiment.polarity == 0):
        neutral += 1
        #print(analysis)

    elif (analysis.sentiment.polarity < 0.00):
        negative += 1
        print(analysis)

    elif (analysis.sentiment.polarity > 0.00):
        positive += 1
        #print(analysis)

positive = percentage(positive, noOfTweet)
negative = percentage(negative, noOfTweet)
neutral = percentage(neutral, noOfTweet)
polarity = percentage(polarity, noOfTweet)

positive = format(positive, '.1f')
negative = format(negative, '.1f')
neutral = format(neutral, '.1f')

#Creating PieCart

labels = ['Positive ['+str(positive)+'%]', 'Neutral [' +
          str(neutral)+'%]', 'Negative ['+str(negative)+'%]']
sizes = [positive, neutral, negative]
colors = ['yellowgreen', 'gold', 'red']

patches, texts = plt.pie(sizes, colors=colors, startangle=90)
plt.style.use('default')
plt.legend(patches, labels, loc='best')
plt.title("Sentiment Analysis Result for keyword=  "+keyword+"")
plt.axis('equal')
plt.show()
