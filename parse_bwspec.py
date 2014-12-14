import os
#import numpy as np

#
# Configuration
#

# Directory where all my files are at.
sourceDir = ""
extension = ".txt"

# How many lines are there before the data shows up?
dataStartIndex = 79

# Character used to seperate data entries
token = ";"

# The column of interest
columnIndex = 



# First get the files.
fileNames = [fileName for  fileName in os.listdir(sourceDir) if fileName.endswith(extension)]

#
#Parse the data
#

allData = []

for fileName in fileNames:
	with open(fileName, 'r') as fileHandle:
		data = []
	
		for i, l in enumerate(fileHandle.readlines()):
			if i>=dataStartIndex:
				ll = l.split(token)
				
				# If there are non-flaot values, e.g. "    " in that col, 
				# you're gonna have to do some additional gating here.
				d = float(ll[columnIndex])
				data.append(d)
		
		allData.append(data)
		
		
#
# Do some operations
#

# For more advanced stuff you're gonna need at least numpy.
# max works without.

maxima = [max(data) for data in allData]
overall_max = max(maxima)

print "Maxima for each file: "
for fileName, value in zip(fileNames, maxima):
	print "{0}: {1}".format(fileName, value)

print "\nOverall max: {0}".format(overall_max)