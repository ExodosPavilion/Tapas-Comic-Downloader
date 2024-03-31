#!/bin/env python3

import json, os

'''
This is meant to be a helper script meant to add some features for the tapas-dl.py script
It's in a seperate file because I don't want to touch the original script 
(Though I might edit the original to accomadate some features this adds)

This script will try to implement the following:
 - A Json based database to keep track of downloaded comics/novels
 - Auto organization of images retrived from the website
 - Option to create cbz files from the images
 - Option to provide a file with links the script needs to get chapters from
 - Option to check for updates since last run
    - And do so without downloading the chapters (will have to look into if this is possible)
'''

def loadConfig(configJsonPath):
    config = {}
    
    if os.path.isfile(configJsonPath):
        with open(configJsonPath) as file:
            config = json.load(file)
    else:
        config = initConfig()

    return config

def initConfig():
    initConfig = {}
    initConfig["persistCharRestriction"] = False
    initConfig["persistVerbose"] = True
    initConfig["useCookies"] = False
    initConfig["cookieTxtLocation"] = "cookies.txt"

    return initConfig

def saveConfig(config, configJsonPath):
    configJsonPath = 'config.json'
    with open(configJsonPath, 'w') as file:
        json.dump(config, file, indent=4)

def loadDatabase(databaseJsonPath):
    database = {}

    if os.path.isfile(databaseJsonPath):
        with open(databaseJsonPath) as file:
            database = json.load(file)

    return database


databaseJsonPath = 'database.json'
configJsonPath = 'config.json'

loadConfig(configJsonPath)