import fsia_test.twittergatherer as twitter

tweet_criteria = twitter.create_twitter_criteria(username="usgs", keywords="florence",since="2018-09-09", until="2018-10-09")
tweet_Criteria2 = twitter.create_twitter_criteria(since="2018-09-09", until="2018-10-09")
print("something")