"""
Created by: Arman B (techtide)
Purpose: Runs the trained network and processes all settings declared in the config file.
Date: 12/10/2018
"""

import os
import numpy as np

API_KEY = ""
DATA_TYPE = ""
REQUEST = ""

LABELS = np.array()

# Parse through the configuration file. Make sure your config follows the rules and style guide described in README.md.
with open('config') as input_file:
    for i, line in enumerate(input_file):
        currLine = line.split()
        if currLine[0] == "api_key":
            API_KEY = currLine[1]
            print("Read API key: " + API_KEY)
        if currLine[0] == "data_type":
            DATA_TYPE = currLine[1]
            print("Read data type: " + DATA_TYPE)
        if currLine[0] == "request":
            REQUEST = currLine[1]
            REQUEST = REQUEST.replace("DEMO_KEY", API_KEY)
            print("Read request url: " + REQUEST)
        if "label" in currLine[0]:
            LABELS.add(currLine[1])

def get_key():
    return API_KEY

def set_key(val):
    global API_KEY
    API_KEY = val

def get_data_type():
    return DATA_TYPE

def set_data_type(val):
    global DATA_TYPE
    DATA_TYPE = val

def get_request_url():
    return REQUEST

def set_request_url(val):
    global REQUEST
    REQUEST = val

def get_labels():
    return LABELS

# Set the environment variable for Bowshock.
os.environ["NASA_API_KEY"] = API_KEY