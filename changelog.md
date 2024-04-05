# How the Versions are Numbered
The versions are numbered as follows: x.y.z
- where x is any major milestone
- where y is any minor milestone
- where z is changes done between minor milestones

# Change Log (from when I made changes)
- v.0.0.1
	- Added gitignore file for python
 		- I plan on using a virtual environment hence the need for a gitignore file so that the venv folder doens't get added to the repo
- v.0.1.0
	- Created the helper script
 		- This script is meant to give additional features for the tapas-dl script
   		- It has a section in the begining that goes over what I want it to do
- v.0.1.1
	- Added some functions to the helper script.
 		- Started adding some CRUD functions for the database and config file
 	- Added some more comments to the tapas-dl script to better understand it
  		- I went over the script to understand what it does and added some comments so that its easier to understand
- v.0.1.2
	- Added a new entry to the gitignore file.
 		- The database.json file is unique for each user hence I added it to the gitignore file
	- Clarified a comment on the helper script.
 		- I mentioned in an earlier commit in that comment that I don't want to alter the original tapas-dl script
   		- This is not entirely true since 
	- Added to a comment on the helper script to tell future me something.
 		- Found a hint on how to check for updates without downloading all the pages
- v.0.1.3
	- updated gitignore
 		- Added an entry for cookies.txt and a test folder
- v.0.1.4
	- Updated gitignore.
 		- Changed the test folder to be more generic
 	- Added more functions to the helper.
  		- Flushed out the CRUD functions for the database and config files
		- Added a function that helps call the tapas-dl script
	    - Started woriking on a function to check for updates
  	- Modified tapas-dl to add some functionality and to help with debugging.
  		- Added functions to Read and Update the database file into the tapas-dl script
  	 	- Added some print statements to help with debugging
  	- Modified tapas-dl to deal with an unexpected edgecase
  		- Noticed that if there is an unreleased or chapter coming soon the script will assume that its a novel even though its a commic
  	 	- Added a check to make sure that its properly handled
- v.0.1.5
	- Create changelog.md
 		- Created a file to keep track of all changes and updates done in the project
- v.0.1.6
	- Fixed a spelling mistake
		- I noticed that the config file had a variable name that was misspelled so I changed it and updated the config file
 
