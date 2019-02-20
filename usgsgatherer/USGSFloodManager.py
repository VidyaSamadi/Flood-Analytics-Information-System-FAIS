import requests
from PIL import Image
from io import BytesIO
import pyquery
import pandas as pd
import numpy as np
import usgsgatherer.USGSFloodCriteria as criteria
import cv2
import re
import urllib.request
import time
from usgsgatherer.imageProcessor import imageProcessor

class usgsFloodManager():
    def __init__(self):
        pass     

    def getRealTimeWaterWatch(self):
        try:
            usgs_csv = pd.read_csv("https://waterwatch.usgs.gov/webservices/realtime?region=sc&format=csv")
            usgs_df = pd.DataFrame(usgs_csv)
            usgs_df = usgs_df[usgs_df.flow != 0]
            return usgs_df
        except:
            time.sleep(5)
    def getImageWaterWatch(self):
        rocky_creed_cam = "http://b7b.hdrelay.com/cameras/fa96bb1e-426d-4b40-a820-251713325420/GetOneShot?size=800x450"
        response = requests.get(rocky_creed_cam)
        img = Image.open(BytesIO(response.content)).convert('Gray')
        open_cv_image = np.array(img)
        open_cv_image = open_cv_image[:, :, ::-1].copy() 
        image_show = imageProcessor.autoAdustment(open_cv_image)
        cv2.imshow('image',image_show)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print()
    
    def getFloodDataCSV(self, USGS_criteria):
        url = "https://waterdata.usgs.gov/"
        url_criteria = ''
        if hasattr(USGS_criteria, 'region'):
            url_criteria += USGS_criteria.region + '/nwis/uv?'
        else:
            url_criteria += 'sc/nwis/'

        if hasattr(USGS_criteria, 'parameters'):
            for parameter in USGS_criteria.parameters:                
                url_criteria += 'cb_' + parameter + '=on&'
        
        url_criteria += 'format=rdb&'

        if hasattr(USGS_criteria, 'station_number'):
            url_criteria += 'site_no='+ USGS_criteria.station_number+ '&'
        
        if hasattr(USGS_criteria, 'since') and hasattr(USGS_criteria, 'until'):
            url_criteria += 'period=&begin_date=' + str(USGS_criteria.since) + '&end_date=' + str(USGS_criteria.until)
        
        url += url_criteria
        text = urllib.request.urlopen(url)
        f = open("flood_old.csv", "w+")
        for line in text:
            line = line.decode('utf-8')
            if line[0] == '#':
                pass
            else:
                temp = line.replace('\t', ',')
                f.writelines(temp)
        f.close()
  

