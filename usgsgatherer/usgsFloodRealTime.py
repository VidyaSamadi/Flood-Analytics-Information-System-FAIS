import urllib3
import pyquery
import pandas as pd
import numpy as np

class usgsFloodRealTime():
    def __init__(self):
        pass
    def getWaterWatch(self):
        usgs_csv = pd.read_csv("https://waterwatch.usgs.gov/webservices/realtime?region=21457492&format=csv")
        usgs_df = pd.DataFrame(usgs_csv)
        usgs_df = usgs_df[usgs_df.flow != 0]
        return usgs_df

