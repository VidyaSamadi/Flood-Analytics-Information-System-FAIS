import urllib.request, urllib.parse, urllib.error,urllib.request,urllib.error,urllib.parse,json,re,datetime,sys,http.cookiejar
from pyquery import PyQuery
class TweetModel:
    def __init__(self):
        pass

class TweetManager:

    def __init__(self):
        pass

    @staticmethod
    def getJsonResponse(tweet_criteria, refresh_cursor, cookie_jar, proxy):
        url = "https://twitter.com/i/search/timeline?f=tweets&q=%s&src=typd&%smax_position=%s"
        
        url_get_data = ''
        if hasattr(tweet_criteria, 'username'):
            url_get_data += ' from:' + tweet_criteria.username
        
        if hasattr(tweet_criteria, 'since'):
            url_get_data += ' since:' + tweet_criteria.since

        if hasattr(tweet_criteria, 'until'):
            url_get_data += ' until:' + tweet_criteria.until
            
        if hasattr(tweet_criteria, 'querySearch'):
            url_get_data += ' ' + tweet_criteria.querySearch
            
        if hasattr(tweet_criteria, 'lang'):
            url_lang = 'lang=' + tweet_criteria.lang + '&'
        else:
            url_lang = ''
        url = url % (urllib.parse.quote(url_get_data), url_lang, refresh_cursor)

        headers = [
            ('Host', "twitter.com"),
            ('User-Agent', "Mozilla/5.0 (Windows NT 6.1; Win64; x64)"),
            ('Accept', "application/json, text/javascript, */*; q=0.01"),
            ('Accept-Language', "de,en-US;q=0.7,en;q=0.3"),
            ('X-Requested-With', "XMLHttpRequest"),
            ('Referer', url),
            ('Connection', "keep-alive")
        ]

        if proxy:
            opener = urllib.request.build_opener(urllib.request.ProxyHandler({'http': proxy, 'https': proxy}), urllib.request.HTTPCookieProcessor(cookie_jar))
        else:
            opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie_jar))
        opener.addheaders = headers

        try:
            response = opener.open(url)
            json_response = response.read()
        except:
            print("https://twitter.com/search?q=%s&src=typd" % urllib.parse.quote(url_get_data))
            print("Unexpected error:", sys.exc_info()[0])
            sys.exit()
            return
        jason_data = json.loads(json_response.decode())
        return jason_data
    
    @staticmethod
    def getTweets(tweet_criteria, receive_buffer=None, buffer_length=100, proxy=None):
        refresh_cursor = ''

        results = []
        results_aux = []
        cookie_jar = http.cookiejar.CookieJar()

        active = True

        while active:
            json = TweetManager.getJsonResponse(tweet_criteria, refresh_cursor, cookie_jar, proxy)
            
            if len(json['items_html'].strip()) == 0:
                break
            
            refresh_cursor = json['min_position']
            scraped_tweets = PyQuery(json['items_html'])
            scraped_tweets.remove('div.withheld-tweet')
            tweets = scraped_tweets('div.js-stream-tweet')

            if len(tweets) == 0:
                break
            for tweet_HTML in tweets:
                tweet_PQ = PyQuery(tweet_HTML)
                tweet = TweetModel()

                username = tweet_PQ.attr("data-screen-name")
                text = re.sub(r"\s+", " ", tweet_PQ("p.js-tweet-text").text().replace('# ', '#').replace('@ ', '@'))
                retweets = int(tweet_PQ("span.ProfileTweet-action--retweet span.ProfileTweet-actionCount").attr("data-tweet-stat-count").replace(",", ""))
                likes = int(tweet_PQ("span.ProfileTweet-action--favorite span.ProfileTweet-actionCount").attr("data-tweet-stat-count").replace(",", ""))
                date = int(tweet_PQ("small.time span.js-short-timestamp").attr("data-time"))
                id = tweet_PQ.attr("data-tweet-id")
                permalink = tweet_PQ.attr("data-permalink-path")
                user_id = int(tweet_PQ("a.js-user-profile-link").attr("data-user-id"))
                media = tweet_PQ("div.AdaptiveMedia-photoContainer").attr("data-image-url")
                geo = ''
                geo_span = tweet_PQ('span.Tweet-geo')
                if len(geo_span) > 0:
                    geo = geo_span.attr('titile')
                urls = []
                for link in tweet_PQ("a"):
                    try:
                        urls.append((link.attrib["data-expanded-url"]))
                    except KeyError:
                        pass
                tweet.id = id
                tweet.source = 'https://twitter.com' + permalink
                tweet.username = username
                tweet.text = text
                tweet.created_at = date
                tweet.retweet_count = retweets
                tweet.favorite_count = likes
                tweet.mentions = " ".join(re.compile('(@\\w*)').findall(tweet.text))
                tweet.hashtags = " ".join(re.compile('(#\\w*)').findall(tweet.text))
                tweet.geo = geo
                tweet.urls = ",".join(urls)
                tweet.author_id = user_id
                tweet.media = media
                results.append(tweet)
                results_aux.append(tweet)

                if receive_buffer and len(results_aux) >= buffer_length:
                    receive_buffer(results_aux)
                    results_aux = []

                if tweet_criteria.max_tweets > 0 and len(results) > tweet_criteria.max_tweets:
                    active = False
                    break
        
        if receive_buffer and len(results_aux) > 0:
            receive_buffer(results_aux)

        return results
                




