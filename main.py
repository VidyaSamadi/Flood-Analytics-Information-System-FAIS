from twitter_client import twitterClient
from twitter_analyzer import tweet_analyzer
import tweetgatherer.TweetCriteria as tweet_criteria
import tweetgatherer.TweetManager as tweet_manager
import usgsgatherer.usgsFloodRealTime as flood_real_time
import nasagatherer.NasaManager as nasa
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
import sys
import datetime
import time

if __name__ == "__main__":
    nasa_manager = nasa.NasaGatherer()
    urls = []
    #urls.append("https://hydro1.gesdisc.eosdis.nasa.gov/opendap/FLDAS/FLDAS_VIC025_A_EA_D.001/2019/02/FLDAS_VIC025_A_EA_D.A20190201.001.nc.nc4")
    #urls.append("https://hydro1.gesdisc.eosdis.nasa.gov/opendap/FLDAS/FLDAS_VIC025_A_EA_D.001/2019/02/FLDAS_VIC025_A_EA_D.A20190209.001.nc.nc4")
    #urls.append("https://hydro1.gesdisc.eosdis.nasa.gov/opendap/FLDAS/FLDAS_VIC025_A_EA_D.001/2019/02/FLDAS_VIC025_A_EA_D.A20190208.001.nc.nc4")
    #nasa_manager.getNasaEarthData(urls)
    #nasa_manager.readNasaNetCDF()
    nasa_manager.getEarthData()
    '''
    #This is gathering tweet and USGS water data Dont delete
    twitter_client = twitterClient("weatherchannel")
    api = twitter_client.get_twitter_api()
    twitter_analyzer = tweet_analyzer()
    tweets = api.user_timeline(screen_name="weatherchannel")
    twitter_client.get_image_tweet()
    frames = []
    #get data from weather channel
    tweeter_criteria = tweet_criteria.TweetCriteria()
    tweeter_criteria.setUsername("weatherchannel").setSince("2018-09-07").setUntil("2018-10-7").setMaxTweets(10000)
    tweet = tweet_manager.TweetManager.getTweets(tweeter_criteria)
    df = twitter_analyzer.tweets_to_dataframe(tweet)
    df['sentiment'] = np.array([twitter_analyzer.analyze_sentiment(tweet) for tweet in df['Tweets']])
    frames.append(df)
    time.sleep(1)

    #get data from NWS 
    tweeter_criteria = tweet_criteria.TweetCriteria()
    tweeter_criteria.setUsername("NWS").setSince("2018-09-07").setUntil("2018-10-7").setMaxTweets(10000)
    tweet = tweet_manager.TweetManager.getTweets(tweeter_criteria)
    df = twitter_analyzer.tweets_to_dataframe(tweet)
    df['sentiment'] = np.array([twitter_analyzer.analyze_sentiment(tweet) for tweet in df['Tweets']])
    frames.append(df)
    time.sleep(1)

    #get data from NWSEastern ‏
    tweeter_criteria = tweet_criteria.TweetCriteria()
    tweeter_criteria.setUsername("NWSEastern‏").setSince("2018-09-07").setUntil("2018-10-7").setMaxTweets(10000)
    tweet = tweet_manager.TweetManager.getTweets(tweeter_criteria)
    df = twitter_analyzer.tweets_to_dataframe(tweet)
    df['sentiment'] = np.array([twitter_analyzer.analyze_sentiment(tweet) for tweet in df['Tweets']])
    frames.append(df)
    time.sleep(1)

    #get data from NWSEastern ‏
    tweeter_criteria = tweet_criteria.TweetCriteria()
    tweeter_criteria.setUsername("USGS").setSince("2018-09-07").setUntil("2018-10-7").setMaxTweets(10000)
    tweet = tweet_manager.TweetManager.getTweets(tweeter_criteria)
    df = twitter_analyzer.tweets_to_dataframe(tweet)
    df['sentiment'] = np.array([twitter_analyzer.analyze_sentiment(tweet) for tweet in df['Tweets']])
    frames.append(df)
    time.sleep(1)

    #get data from NWSEastern ‏
    tweeter_criteria = tweet_criteria.TweetCriteria()
    tweeter_criteria.setUsername("NHC_Atlantic").setSince("2018-09-07").setUntil("2018-10-7").setMaxTweets(10000)
    tweet = tweet_manager.TweetManager.getTweets(tweeter_criteria)
    df = twitter_analyzer.tweets_to_dataframe(tweet)
    df['sentiment'] = np.array([twitter_analyzer.analyze_sentiment(tweet) for tweet in df['Tweets']])
    frames.append(df)
    time.sleep(1)
    df = pd.concat(frames)
    df.to_csv('data_twitter.csv')
    '''
    '''
    flood_real_time = flood_real_time.usgsFloodRealTime()
    df = pd.DataFrame(flood_real_time.getWaterWatch())
    df['flow_dt'] = pd.to_datetime(df['flow_dt'])
    df.sort_values('flow_dt')
    i = 0
    frames = []
    frames.append(df)
    #time.sleep(15*60)
    while i <= 192:
        temp_df = pd.DataFrame(flood_real_time.getWaterWatch())
        frames.append(temp_df)
        time.sleep(15*60)
        i = i+1
    df = pd.concat(frames)
    df.to_csv('flood.csv')
    
    flood_real_time = flood_real_time.usgsFloodRealTime()
    flood_real_time.getImageWaterWatch()
    time.sleep(1)

    '''


