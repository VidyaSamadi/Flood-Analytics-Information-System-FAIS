import requests
import nasagatherer.NasaCredential as NasaCredential
import time
import netCDF4

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
    
    def getNasaEarthData(self,urls):
        for url in urls:
            filename = url[url.rfind('/')+1:]
            try:
                response = self.session.get(url, stream=True)
                print(response.status_code)
                with open(filename,'wb') as fd:
                    for chunk in response.iter_content(chunk_size=1024*1024):
                        fd.write(chunk)
            except requests.exceptions.HTTPError as e:
                print(e)
                return
            time.sleep(2)

    def readNasaNetCDF(self):



