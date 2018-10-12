"""
Created by: Arman B (techtide)
Purpose: Makes using data from the NASA APIs as easy as modifying a configuration file.
Date: 11/10/2018
"""

from run import *

import requests
import json
import urllib.request

r = requests.get(get_request_url())

h = json.loads(str(r.text))

if (get_data_type() == 'image'):
    imgurl = h["hdurl"]
    urllib.request.urlretrieve(imgurl, "train/00000001.jpg")
    print(imgurl)