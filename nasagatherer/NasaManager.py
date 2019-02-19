import requests
import nasagatherer.NasaCredential as NasaCredential
import time
import netCDF4
import os
import cv2
import numpy as np
from nasa import earth

class SessionWithHeaderRedirection(requests.Session):
    AUTH_HOST = 'urs.earthdata.nasa.gov'
    def __init__(self, username,password):
        super().__init__()        
        self.auth = (username, password)

    def rebuild_auth(self, prepared_request, response):
        headers = prepared_request.headers
        url = prepared_request.url
        if 'Authorization' in headers:
            original_parsed = requests.utils.urlparse(response.request.url)
            redirect_parsed = requests.utils.urlparse(url)      

            if(original_parsed.hostname != redirect_parsed.hostname) and (redirect_parsed.hostname != self.AUTH_HOST) and (original_parsed.hostname != self.AUTH_HOST):
                del headers['Authorization']
        
        return

class NasaGatherer():
    def __init__(self):
        self.username = NasaCredential.NASA_USERNAME
        self.password = NasaCredential.NASA_PASSWORD
        self.session = SessionWithHeaderRedirection(self.username, self.password)
        os.environ["NASA_API_KEY"] = "zqiIogJ4ANsA17OwAvWFYT1ijYHhndlRACafWYKj"

    
    def getNasaEarthData(self,urls):
        for url in urls:
            filename = url[url.rfind('/')+1:]
            try:
                response = self.session.get(url, stream=True)
                with open(filename,'wb') as fd:
                    for chunk in response.iter_content(chunk_size=1024*1024):
                        fd.write(chunk)
            except requests.exceptions.HTTPError as e:
                print(e)
                return
            time.sleep(2)

    def readNasaNetCDF(self):
        rootgrp = netCDF4.Dataset("FLDAS_VIC025_A_EA_D.A20190201.001.nc.nc4", "a" , format="NETCDF4")
        print(rootgrp.file_format)

    def getEarthData(self):
        filter_specification = earth.assets(lat=34.0, lon=-81.0, begin='2015-09-14', end='2015-10-22')
        images = []
        i = 0
        for a in filter_specification:
            images.append(a.get_asset_image())
        for image in images:
            image.image.show()
        return



