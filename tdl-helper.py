#!/bin/env python3

import json, os, re, subprocess, sys
from datetime import datetime

'''
This is meant to be a helper script meant to add some features for the tapas-dl.py script
I will edit the original script to assist with the additional functionality I'm adding
However I wish for the original script to run independently when necessary and the helper script to simply help it along

This script will try to implement the following:
 - A Json based database to keep track of downloaded comics/novels
 - Auto organization of images retrived from the website 
    - Such as putting them in folders organised by chapter number
 - Option to create cbz files from the images
 - Option to provide a file with links the script needs to get chapters from
 - Option to check for updates since last run
    - And do so without downloading the chapters 
        - Will have to look into if this is possible
        - Seems possible, will have to save the pageOffset or the pageCount in the database
'''

# --------------- CONFIG ACTIONS  ---------------
# All funcitons that mess with the config
# dictionary and the config json file
# --------------- --------------- ---------------
def loadConfig(configJsonPath = 'config.json'):
    # Load the config data from the json file
    config = {}
    
    if os.path.isfile(configJsonPath):
        with open(configJsonPath) as file:
            config = json.load(file)
    else:
        config = initConfig(configJsonPath)

    return config

def initConfig(configJsonPath = 'config.json'):
    # Initialize the config json file if it doesn't exist
    initConfig = {}
    initConfig["persistCharRestriction"] = False
    initConfig["persistVerbose"] = True
    initConfig["useCookies"] = False
    initConfig["cookieTxtLocation"] = "cookies.txt"
    initConfig["chagneOutput"] = True
    initConfig["outputLocation"] = "DL-Dir"

    saveConfig(initConfig, configJsonPath)

    return initConfig

def saveConfig(config, configJsonPath = 'config.json'):
    # Save the config data
    with open(configJsonPath, 'w') as file:
        json.dump(config, file, indent=4)

# --------------- --------------- ---------------
# --------------- CONFIG ACTIONS  ---------------

# --------------- DATABASE ACTIONS ---------------
# All commands that mess with the database dictionary
# and the database json file
# --------------- ---------------- ---------------
def loadDatabase(databaseJsonPath = 'database.json'):
    # Load the database from the json file
    database = {}

    if os.path.isfile(databaseJsonPath):
        with open(databaseJsonPath) as file:
            database = json.load(file)
    else:
        database = initDatabase(databaseJsonPath)

    return database

def savedatabase(database, databaseJsonPath = 'database.json'):
    # Save the database data
    with open(databaseJsonPath, 'w') as file:
        json.dump(database, file, indent=4)

def initDatabase(databaseJsonPath = 'database.json'):
    # Initialize the database file if it doesn't exist
    initDatabase = {}
    initDatabase["comics"] = []
    initDatabase["comicsLastID"] = -1
    initDatabase["novels"] = []
    initDatabase["novelsLastID"] = -1
    initDatabase["updateCheckedDate"] = datetime.now().isoformat()

    savedatabase(initDatabase, databaseJsonPath)

    return initDatabase

def convertTime(database):
    # Convert the time strings in the database to python usable objects
    for item in database['comics']:
        item["lastCheckedDate"] = datetime.fromisoformat(item["lastCheckedDate"])

    for item in database['novels']:
        item["lastCheckedDate"] = datetime.fromisoformat(item["lastCheckedDate"])
    
    database['updateCheckedDate'] = datetime.fromisoformat(item["updateCheckedDate"])

    return database

def createDataEntry(url, lastID, comic = True, pageCount = 0, lastCheckedDate = datetime.now().isoformat()):
    # Create an entry for either comics or novels with the relevant data
    dataEntry = {}
    
    if url != '':
        dataEntry['id'] = lastID + 1
        dataEntry["name"] = getNameFromURL(url)
        dataEntry["url"] = url
        dataEntry["lastCheckedDate"] = lastCheckedDate
        if comic:
            dataEntry["pageCount"] = pageCount
    
    return dataEntry

# --------------- ----------------- ---------------
# --------------- DATABASE ACTIONS  ---------------


def getNameFromURL(url):
    # Extract the name of the item from the url
    urlName = ''
    # check url/name
    if re.match(r'^https://tapas\.io/series/.+$', url):
        urlName = (url[url.rindex('/') + 1:]).replace('-', ' ').title()
    else:
        urlName = url.replace('-', ' ').title()

    return urlName

def loadCommand(url = '', config = {}):
    # Create a list for all the arguments that need to be called when running tapas-dl
    command = []
    if url != '' and config != {}:
        command = ['python', 'tapas-dl.py', url, '-e']
        if config['persistCharRestriction']:
            command.append('-r')
        if config['persistVerbose']:
            command.append('-v')
        if config['useCookies']:
            command.append('-c')
            command.append(config['cookieTxtLocation'])
        if config['chagneOutput']:
            command.append('-o')
            command.append(config['outputLocation'])

    return command

def callScript(command = []):
    # Run the tapas-dl script and manage all relevant errors
    if(command != []):
        try:
            subprocess.check_call(command, stdout=sys.stdout, stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as e:
            print("Command failed with return code:", e.returncode)
            # Print a descriptive message for the custom error code
            if e.returncode == 1:
                print("Database Missing: Make sure that the database exists before calling it")


def checkForUpdates(database = {}, config = {}):
    # Check if there are any updates for available for the script to download
    if database != {} and config != {}:
        if database['updateCheckedDate'] != datetime.now().isoformat():

            for comic in database['comics']:
                print(f'\nChecking updates for {comic['name']}')
                callScript(loadCommand(comic['url'], config))

            for novel in database['novels']:
                print(f'\nChecking updates for {novel['name']}')
                callScript(loadCommand(novel['url'], config))

            database['updateCheckedDate'] = datetime.now().isoformat()


databaseJsonPath = 'database.json'
configJsonPath = 'config.json'

config = loadConfig(configJsonPath)
database = loadDatabase(databaseJsonPath)

'''
url = 'https://tapas.io/series/the-resourceful-little-consort'
database['comics'].append(createDataEntry(url, database['comicsLastID']))
savedatabase(database, databaseJsonPath)

command = loadCommand(url, config)

if(command != []):
    subprocess.check_call(command, stdout=sys.stdout, stderr=subprocess.STDOUT)
'''

checkForUpdates(database, config)