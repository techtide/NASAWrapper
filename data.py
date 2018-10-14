"""
Created by: Arman B (techtide)
Purpose: Makes using data from the NASA APIs as easy as modifying a configuration file.
Date: 11/10/2018
"""

from run import *

import requests
import json
import urllib.request



array1 = [[],[]]

if (get_data_type() == 'image'):
    i = 1
    opznum = 10
    while i <= 20:
        print(get_request_url())
        rurl = get_request_url()
        r = requests.get(get_request_url())
        h = json.loads(str(r.text))
        d = h["date"]
        opz = ""
        if i < opznum:
            opz = "0"
        d1 = d[:-2] + opz + str(i+1)
        if d1 != d[:-2] + "21":
            if "hdurl" not in h:
                print("not img")
                set_request_url(rurl[:-10] + d1)
                i = i+1
                opznum = opznum-1
                continue
            else:
                imgurl = h["hdurl"]
                imgnum = i
                urllib.request.urlretrieve(imgurl, "train/" + str(imgnum) + ".jpg")
                print(imgurl)
        set_request_url(rurl[:-10] + d1)
        i = i+1