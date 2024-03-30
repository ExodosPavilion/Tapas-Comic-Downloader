#!/bin/env python3

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