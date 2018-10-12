"""
Created by: Arman B (techtide)
Purpose: Runs the trained network and processes all settings declared in the config file.
Date: 11/10/2018
"""

import os

API_KEY = ""
DATA_TYPE = ""
REQUEST = ""

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
            print("Read request url: " + REQUEST)

def get_key():
    return API_KEY

def get_data_type():
    return DATA_TYPE

def get_request_url():
    return REQUEST

# Set the environment variable for Bowshock.
os.environ["NASA_API_KEY"] = API_KEY