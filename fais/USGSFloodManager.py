import requests
from PIL import Image
from io import BytesIO
import pyquery
import pandas as pd
import numpy as np
import fsia.usgsgatherer.USGSFloodCriteria as criteria
import cv2
import re
import time
import json
import http
import urllib
from fsia.usgsgatherer.imageProcessor import imageProcessor

class imageWaterWatchModel():
    def __init__(self):
        self.id = ""
        self.link = ""

    def setLink(self, link):
        self.link = link
        return self
    def setID(self, id):
        self.id = id
        return self

class usgsFloodManager():
    def __init__(self):
        self.cameras = []
        rocky_creed_cam = imageWaterWatchModel().setLink("http://b7b.hdrelay.com/cameras/fa96bb1e-426d-4b40-a820-251713325420/GetOneShot?size=800x450").setID("021603273")
        lake_moultrie_cam = imageWaterWatchModel().setLink("http://b7b.hdrelay.com/cameras/dab6dc0d-d702-4146-899f-85a7945de140/GetOneShot?size=800x450").setID("02172002")
        rocky_branch_Whalet_cam = imageWaterWatchModel().setLink("http://b7b.hdrelay.com/cameras/2fb4ae88-446d-4632-a849-d426240ccca5/GetOneShot?size=800x450").setID("02169506")
        peedee_river_cam = imageWaterWatchModel().setLink("http://b6b.hdrelay.com/cameras/42336a6b-5be8-443c-97c9-3d70da459e88/GetOneShot?size=800x450").setID("02130810")
        lake_moultrie_trail_canell_cam = imageWaterWatchModel().setLink("http://b7b.hdrelay.com/cameras/dab6dc0d-d702-4146-899f-85a7945de140/GetOneShot?size=800x450").setID("02172002")
        tearcoat_branch_upstream_cam = imageWaterWatchModel().setLink("http://b6b.hdrelay.com/cameras/403818bc-9e8d-4857-9eb0-a675c9668782/GetOneShot?size=800x450").setID("021355015_1")
        tearcoat_branch_downstream_cam = imageWaterWatchModel().setLink("http://b6b.hdrelay.com/cameras/009e9855-a077-4c2a-8289-10eea8ba9f0f/GetOneShot?size=800x450").setID("021355015_2")
        pocotaligo_river_upstream_cam = imageWaterWatchModel().setLink("http://b6b.hdrelay.com/cameras/a8a00672-f089-4b2d-bf36-85e41a838488/GetOneShot?size=800x450").setID("02135615_1")
        pocotaligo_river_downstream_cam = imageWaterWatchModel().setLink("http://b6b.hdrelay.com/cameras/39f23793-0e60-43f6-a0b4-ccb073004640/GetOneShot?size=800x450").setID("02172002_1")
        self.cameras.append(rocky_creed_cam)
        self.cameras.append(lake_moultrie_cam)
        self.cameras.append(rocky_branch_Whalet_cam)
        self.cameras.append(peedee_river_cam)
        self.cameras.append(lake_moultrie_trail_canell_cam)
        self.cameras.append(tearcoat_branch_upstream_cam)
        self.cameras.append(tearcoat_branch_downstream_cam)
        self.cameras.append(pocotaligo_river_upstream_cam)
        self.cameras.append(pocotaligo_river_downstream_cam)

    def getRealTimeWaterWatch(self):
        try:
            usgs_csv = pd.read_csv("https://waterwatch.usgs.gov/webservices/realtime?region=sc&format=csv")
            usgs_df = pd.DataFrame(usgs_csv)
            usgs_df = usgs_df[usgs_df.flow != 0]
            return usgs_df
        except:
            time.sleep(5)
    def getImageWaterWatch(self, id):
        selected_cam = imageWaterWatchModel()
        for cam in self.cameras:
            if cam.id == id:
                selected_cam = cam
        if selected_cam.id == "":
            print("ERROR, camera do not exist")
            return False
        else:
            response = requests.get(selected_cam.link)
            img = Image.open(BytesIO(response.content))
            open_cv_image = np.array(img)
            open_cv_image = open_cv_image[:, :, ::-1].copy()
            img_gray = cv2.cvtColor(open_cv_image, cv2.COLOR_BGR2GRAY)
            cv2.imshow('image',img_gray)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

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
