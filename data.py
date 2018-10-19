"""
Created by: Arman B (techtide) && SRugina
Purpose: Makes using data from the NASA APIs as easy as modifying a configuration file.
Date: 11/10/2018
"""

from run import *

import requests
import json
import urllib.request

import tkinter as tk
from PIL import ImageTk, Image

def show_imge(path):
    image_window = tk.Tk()
    imgr = Image.open(path)
    imgr = imgr.resize((1280,720), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(imgr)
    panel = tk.Label(image_window, image=img, height=720, width=1280)
    panel.pack(side="bottom", fill="both", expand="yes")
    image_window.mainloop()

array1 = []  # this has the labels

trainortestval = str(get_train_or_test())

if (get_data_type() == 'image'):
    i = 1
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
            temparray = [0, 0, 0]
            imgurl = h["hdurl"]
            imgnum = i
            urllib.request.urlretrieve(imgurl, trainortestval + "/" + str(imgnum) + ".jpg")
            show_imge(trainortestval + "/" + str(imgnum) + ".jpg")
            print(h["explanation"])
            labelornot = int(input("Which label should we assign? (0=skip image, 1=" + str(get_labels()[0]) + ", 2=" + str(get_labels()[1]) + ", 3=" + str(get_labels()[2]) + ", 4=" + str(get_labels()[3])))
            if labelornot != 0:
                temparray[0] = trainortestval + "/" + str(imgnum) + ".jpg"
                label_options = get_labels()
                labelstr = str(get_labels()[labelornot-1])
                labelstr = labelstr[2:]
                labelstr = labelstr[:-2]
                temparray[1] = labelstr
                temparray[2] = trainortestval
                array1.append(temparray)
                print(imgurl)
                dval = dval+1
                if (dval < opznum):
                    opz = "0"
                else:
                    opz = ""
                d2 = d[:-2] + opz + str(dval)
            else:
                os.remove(trainortestval + "/" + str(imgnum) + ".jpg")
                dval = dval+1
                if (dval < opznum):
                    opz = "0"
                else:
                    opz = ""
                d2 = d[:-2] + opz + str(dval)
                set_request_url(rurl[:-10] + d2)
                continue
        set_request_url(rurl[:-10] + d2)
        i = i+1
    if i > 20:
        print(array1)
elif (get_data_type() == 'text'):
    #pseudo code
    r1 = requests.get(get_request2_url())
    h1 = json.loads(str(r1.text))
    d1 = h1["diameter"]
    l1 = h1["type"]
    temparray = [0, 0, 0]
    temparray[0] = d1
    temparray[1] = l1
    temparray[2] = trainortestval
    array1.append(temparray)
    print(array1)