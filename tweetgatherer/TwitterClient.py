from tweepy import API
from tweepy import Cursor
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import TweepError
from twitter_analyzer import tweet_analyzer
import time
import twitterkeys
import pandas as pd

"""
Twitter Client class will authenticate and return twitter client object
"""
class twitterClient():
    def __init__(self, twitter_user_screenname):
        # Authentication Process from Twitter
        self.auth = OAuthHandler(twitterkeys.CONSUMER_KEY, twitterkeys.CONSUMER_SECRET)
        self.auth.set_access_token(twitterkeys.ACCESS_TOKEN, twitterkeys.ACCESS_TOKEN_SECRET)
        self.twitter_client = API(self.auth)
        # Definded Specific User
        self.twitter_user = twitter_user_screenname

    def get_twitter_api(self):
        #return twitter API
        return self.twitter_client

    def get_tweets(self, num_tweet=0):
        #return tweet by the specific user or self
        tweets = []
        if num_tweet == 0:
            tweets = Cursor(self.twitter_client.user_timeline,id=self.twitter_user)
        else:
            for tweet in Cursor(self.twitter_client.user_timeline,id=self.twitter_user).items(num_tweet):
                tweets.append(tweet)
        return tweets

    def get_friend_list(self, num_friends):
        #return Friend list by the specific user or self
        friends = []
        for friend in Cursor(self.twitter_client.friends,id=self.twitter_user).items(num_friends):
            friends.append(friend)
        return friends

    def get_home_tweets(self, num_tweet):
        #return home page tweet list by the specific user or self
        home_tweets = []
        for tweet in Cursor(self.twitter_client.home_timeline,id=self.twitter_user).items(num_tweet):
            home_tweets.append(tweet)
        return home_tweets

    def get_tweets_between_date(self, start, end):
        tweets = []
        c = Cursor(self.twitter_client.user_timeline, id=self.twitter_user).items()
        while True:
            try:
                tweet = c.next()
                if tweet.created_at < end and tweet.created_at > start:
                    tweets.append(tweet)
                if tweet.created_at <= start:
                    return tweets
                time.sleep(0.15)
            except TweepError:
                time.sleep(60*15)
                continue
            except StopIteration:
                return tweets

    def get_tweets_between_date2(self, start, end):
        df = pd.DataFrame()
        c = Cursor(self.twitter_client.user_timeline, id=self.twitter_user).pages()
        analyzer = tweet_analyzer()
        while True:
            try:
                tweets_list = c.next()
                tweets = []
                for tweet in tweets_list:                
                    if tweet.created_at < end and tweet.created_at > start:
                        tweets.append(tweet)
                    elif tweet.created_at < start:
                        return df
                if len(tweets) != 0:
                    temp = analyzer.tweets_to_dataframe(tweets)
                    if df.empty:
                        df = temp
                    else:                        
                        df.append(temp, ignore_index=True)
                time.sleep(0.15)
            except TweepError:
                time.sleep(60*15)
                continue
            except StopIteration:
                return df
                
    def get_image_tweet(self):
        tweets = []
        c = Cursor(self.twitter_client.user_timeline, id=self.twitter_user, include_entities=True).pages()
        tweets = c.next()
        for tweet in tweets:
            if 'media' in tweet.entities:
                for image in tweet.entities['media']:
                    print(image['media_url'])
                    



     

"""
Class For streaming and processing tweets
"""
class tweetStreamer():
    def __init__(self):
        self.twitter_authenticator = twitterAuthenticator()

    def stream_tweets(self, filename, hashtag_list):
        #handle twitter authentication
        listener = twitterListener(filename)
        auth = self.twitter_authenticator.authenticate_twitter()
        stream = Stream(auth, listener)
        stream.filter(track=hashtag_list)

class twitterAuthenticator():
    """
    Authenticate Class for Tweepy
    """
    def authenticate_twitter(self):
        auth = OAuthHandler(twitterkeys.CONSUMER_KEY, twitterkeys.CONSUMER_SECRET)
        auth.set_access_token(twitterkeys.ACCESS_TOKEN, twitterkeys.ACCESS_TOKEN_SECRET)
        return auth

class twitterListener(StreamListener):
        """
        Basic listener class that just prints received tweets to stdout 
        """
        def __init__(self, fetched_tweets_filename):
            self.fetched_tweets_filename = fetched_tweets_filename
                
        def on_data(self,data):
            try:
                print(data)
                with open(self.fetched_tweets_filename, 'a') as tf:
                    tf.write(data)
                return True 
            except BaseException as e:
                print("error on_data %s" % str(e))
            return True

        def on_error(self, status):
                if status == 420:
                    #return false on_data method in case of rate limit occurs
                    return False
                print(status)        
