from fais import nasagatherer as nasa
from fais import usgsgatherer as usgs
from fais import twittergatherer as twitter
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
import sys
import datetime
import time

if __name__ == "__main__":
    #twitter_username = None
    #twitter_keyword = "Florence"
    #twitter_since = "2018-09-20"
    #twitter_until = "2018-10-20"
    #twitter_criteria = twitter.create_twitter_criteria(twitter_username, twitter_keyword,twitter_since,twitter_until, 10000)
    #print(twitter_criteria)
    #twitter.get_tweets_csv(twitter_criteria, "florence")
    #usgs_criteria = usgs.create_usgs_criteria("SC","02130561", ["0065"], "2018-09-20", "2018-10-20")
    #usgs.get_realtime_flood_csv("nc","ncrealtime.csv")
    usgs.get_station_list_dataframe("nc")
    


