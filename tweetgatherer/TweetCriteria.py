class TweetCriteria:

	def __init__(self):
		self.max_tweets = 0

	def setUsername(self, username):
		self.username = username
		return self

	def setSince(self, since):
		self.since = since
		return self

	def setUntil(self, until):
		self.until = until
		return self

	def setQuerySearch(self, querySearch):
		self.querySearch = querySearch
		return self

	def setMaxTweets(self, max_tweets):
		self.max_tweets = max_tweets
		return self

	def setLang(self, Lang):
		self.lang = Lang
		return self

	def setTopTweets(self, topTweets):
 		self.topweets = topTweets
 		return self
