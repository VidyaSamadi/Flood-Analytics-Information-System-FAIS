#	Set up the Criteria for USGS Search the Setting that is possible are
#	Username, Time Gap, Query, Language, Max Tweets for data return
#	The Function is then send the Criteria TweetManager.py

class usgsCriteria:
    def __init__(self):
        pass

    def setRegion(self, region):
        self.region = region
        return self

    def setSince(self, since):
        self.since = since
        return self
    
    def setUntil(self, until):
        self.until = until
        return self

    def setStationNumber(self, station_number):
        self.station_number = station_number
        return self
    
    def setParameters(self, parameters):
        self.parameters = parameters
        return self
    

