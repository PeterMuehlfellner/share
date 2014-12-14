# Instructions for Windows:
# 1) Install Anaconda (http://continuum.io/downloads)
# 2) Adjust configuration (i.e. set correct directories and stuff below).
# 3) Run IPython (Start -> IPython)
# 4) Type "cd where-ever-this-file-is"
# 5) Type "run parse_bwspec.py"
# 6) ???
# 7) Profit!

import os

hasMatplotlib=True
if hasMatplotlib: 
	import numpy as np
	import pylab as pl

#
# Configuration
#

# Directory where all my files are at.
sourceDir = "D:/git/share/test"
extension = ".txt"

# How many lines are there before the data shows up?
dataStartIndex = 79

# Character used to seperate data entries
token = ";"

# The column of interest
columnIndex = 6



#
#Parse the data
#
fileNames = [fileName for  fileName in os.listdir(sourceDir) if fileName.endswith(extension)]

allData = []

for fileName in fileNames:
	with open(os.path.join(sourceDir, fileName), 'r') as fileHandle:
		data = []
	
		for i, l in enumerate(fileHandle.readlines()):
			if i>=dataStartIndex:
				ll = l.split(token)
				
				# If there are non-float values, e.g. "    " in that col, 
				# you're gonna have to do some additional gating here.
				# The replace is for the German style commas.
				d = float(ll[columnIndex].replace(",", "."))
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


if hasMatplotlib:
	# Make everything numpy arrays. These are basically like MATLAB matrices.
	D = np.array(allData)

	pl.figure()
	pl.title("Frobonication")
	pl.xlabel("Penile Length")
	pl.ylabel("Average Fr.")
	for fileName, d in zip(fileNames, D):
		pl.plot(d, label=fileName)
	
	pl.legend()
	pl.show()
	