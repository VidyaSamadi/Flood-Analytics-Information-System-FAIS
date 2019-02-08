import requests
from PIL import Image
from io import BytesIO
import pyquery
import pandas as pd
import numpy as np
import cv2
import re

class usgsFloodRealTime():
    def __init__(self):
        pass     

    def getWaterWatch(self):
        usgs_csv = pd.read_csv("https://waterwatch.usgs.gov/webservices/realtime?region=sc&format=csv")
        usgs_df = pd.DataFrame(usgs_csv)
        usgs_df = usgs_df[usgs_df.flow != 0]
        return usgs_df
    def getImageWaterWatch(self):
        rocky_creed_cam = "http://b7b.hdrelay.com/cameras/fa96bb1e-426d-4b40-a820-251713325420/GetOneShot?size=800x450"
        response = requests.get(rocky_creed_cam)
        img = Image.open(BytesIO(response.content)).convert('RGB')
        open_cv_image = np.array(img)
        open_cv_image = open_cv_image[:, :, ::-1].copy() 
        
        cv2.imshow('image',open_cv_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print()
        


