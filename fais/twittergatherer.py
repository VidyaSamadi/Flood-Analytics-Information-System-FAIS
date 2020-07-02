import fais.TwitterClient as client
import fais.TweetManager as manager
import fais.TweetModel as model
import fais.TweetCriteria as search_criteria
import fais.TweetAnalyzer as analyzer
import pandas as pd
import numpy as np

#   Create the criteria for twitter search
#   This criteria is used in getting twitter data
#   Return the empty criteria if not successfully
def create_twitter_criteria(username=None,keywords=None, since=None, until=None,max_tweet=1000):
    tweet_criteria = search_criteria.TweetCriteria()
    is_valid = False
    if username != None:
        tweet_criteria.setUsername(username)
        is_valid = True
    if keywords != None:
        tweet_criteria.setQuerySearch(keywords)
        is_valid = True
    if is_valid == False:
        print("The criteria is not valid please enter The username or Keywords")
        return tweet_criteria
    if since != None:
        tweet_criteria.setSince(since)
    if until != None:
        tweet_criteria.setUntil(until)
    tweet_criteria.setMaxTweets(max_tweet)
    return tweet_criteria

def update_username(criteria=None,username=None):
    if criteria == None:
        print("Criteria missing please include the criteria")
        return
    if username == None:
        print("Username missing")
        return
    criteria.setUsername(username)
    return criteria

def update_keyword(criteria=None,keyword=None):
    if criteria == None:
        print("Criteria missing please include the criteria")
        return
    if keyword == None:
        print("Keyword missing")
        return
    criteria.setQuerySearch(keyword)
    return criteria

def update_since(criteria=None,since=None):
    if criteria == None:
        print("Criteria missing please include the criteria")
        return
    if since == None:
        print("Since missing")
        return
    criteria.setSince(since)
    return criteria

def update_until(criteria=None,until=None):
    if criteria == None:
        print("Criteria missing please include the criteria")
        return
    if until == None:
        print("Until missing")
        return
    criteria.setUntil(until)
    return criteria

def update_maxTweet(criteria=None,max_tweet=None):
    if criteria == None:
        print("Criteria missing please include the criteria")
        return
    if max_tweet == None:
        print("Until missing")
        return
    criteria.setMaxTweets(max_tweet)
    return criteria

def get_tweets_dataframe(criteria):
    twitter = analyzer.tweet_analyzer()
    tweet = manager.TweetManager.getTweets(criteria)
    df = twitter.tweets_to_dataframe(tweet)
    df['sentiment'] = np.array([twitter.analyze_sentiment(tweet) for tweet in df['Tweets']])
    return df

def get_tweets_csv(criteria, filename):
    df = get_tweets_dataframe(criteria)
    if ".csv" not in filename:
        filename = filename + ".csv"
    df.to_csv(filename) 
