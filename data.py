"""
Created by: Arman B (techtide) && SRugina
Purpose: Makes using data from the NASA APIs as easy as modifying a configuration file.
Date: 11/10/2018
"""

from run import *

import requests
import json
import urllib.request




if (get_data_type() == 'image'):
    i = 1
    #icba to do the array properly
    array1 = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
    r1 = requests.get(get_request_url())
    h1 = json.loads(str(r1.text))
    d1 = h1["date"]
    dval = int(d1[-2:])
    opznum = 10
    while i <= 20:
        print(get_request_url())
        rurl = get_request_url()
        r = requests.get(get_request_url())
        h = json.loads(str(r.text))
        d = h["date"]
        opz = ""
        if (dval < opznum):
            opz = "0"
        else:
            opz = ""
        d2 = d[:-2] + opz + str(dval)
        if ("hdurl" not in h):
            print("not img")
            dval = dval+1
            if (dval < opznum):
                opz = "0"
            else:
                opz = ""
            d2 = d[:-2] + opz + str(dval)
            set_request_url(rurl[:-10] + d2)
            continue
        else:
            imgurl = h["hdurl"]
            imgnum = i
            urllib.request.urlretrieve(imgurl, "train/" + str(imgnum) + ".jpg")
            array1[imgnum-1][0] = "train/" + str(imgnum) + ".jpg"
            array1[imgnum-1][1] = "somelabel"
            array1[imgnum-1][2] = "training"
            print(imgurl)
            dval = dval+1
            if (dval < opznum):
                opz = "0"
            else:
                opz = ""
            d2 = d[:-2] + opz + str(dval)
        set_request_url(rurl[:-10] + d2)
        i = i+1
    if i > 20:
        print(array1)