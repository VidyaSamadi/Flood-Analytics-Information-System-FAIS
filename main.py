from twitter_client import twitterClient
from twitter_analyzer import tweet_analyzer
import tweetgatherer.TweetCriteria as tweet_criteria
import tweetgatherer.TweetManager as tweet_manager
import usgsgatherer.usgsFloodRealTime as flood_real_time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
import sys
import datetime
import time

if __name__ == "__main__":
    twitter_client = twitterClient("weatherchannel")
    api = twitter_client.get_twitter_api()
    twitter_analyzer = tweet_analyzer()
    tweets = api.user_timeline(screen_name="weatherchannel")
    twitter_client.get_image_tweet()

    #tweet_criteria = tweet_criteria.TweetCriteria()
    #tweet_criteria.setUsername("weatherchannel").setSince("2018-09-07").setUntil("2018-10-7").setMaxTweets(10000)
    #tweet = tweet_manager.TweetManager.getTweets(tweet_criteria)
    #tweet_criteria.setUsername("weatherchannel").setSince("2018-09-07").setUntil("2018-10-7").setMaxTweets(10000)
    #tweet = tweet_manager.TweetManager.getTweets(tweet_criteria)
    #df = twitter_analyzer.tweets_to_dataframe(tweet)
    #df.to_csv("data2.csv")
    flood_real_time = flood_real_time.usgsFloodRealTime()
    df = pd.DataFrame(flood_real_time.getWaterWatch())
    df['flow_dt'] = pd.to_datetime(df['flow_dt'])
    df.sort_values('flow_dt')
    df.to_csv('flood.csv')
