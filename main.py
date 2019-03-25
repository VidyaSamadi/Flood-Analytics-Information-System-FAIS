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
    twitter_username = None
    twitter_keyword = "Florence"
    twitter_since = "2018-09-20"
    twitter_until = "2018-10-20"
    twitter_criteria = twitter.create_twitter_criteria(twitter_username, twitter_keyword,twitter_since,twitter_until, 10000)
    print(twitter_criteria)
    twitter.get_tweets_csv(twitter_criteria, "florence")
    


