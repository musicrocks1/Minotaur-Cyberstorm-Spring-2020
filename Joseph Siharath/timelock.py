# Name: Joseph Siharath
# Due Date: 5/8/20
# Description: This program takes an epoch time and current time or manual set and finds the elasped time 
# and uses that to create a hash to create a code 

# NOTE: This program uses python2.7
from sys import stdin
from datetime import datetime
import pytz
from hashlib import md5


# Debugger
DEBUG = False

# Interval of time
interval = 60

# Local Timezone and Daylight Savings Time
localtz = pytz.timezone("US/Central")
DST = True

# Seconds in a Day
SECONDS = (24*60*60)

# Current Date Setter
MANUAL = False
MANUAL_DATETIME = "2013 05 06 07 43 25"

# Getting the EPOCH Date
EPOCH = stdin.read().rstrip("\n")

# Getting the current time in UCT
curTime = datetime.utcnow()

# Converting Epoch Time
epochTime = datetime.strptime(EPOCH, "%Y %m %d %H %M %S")

# NOTE: it is important to change the Daylight Savings Time Constant if you are in or not in DST 
localEpochTime = localtz.localize(epochTime, is_dst=DST)
utcEpochTime = localEpochTime.astimezone(pytz.utc)

# If Manual date is set, use a manual time and calculate the elasped seconds
if (MANUAL == True):
	manTime = datetime.strptime(MANUAL_DATETIME, "%Y %m %d %H %M %S")

	localManTime = localtz.localize(manTime, is_dst=DST)
	utcManTime = localManTime.astimezone(pytz.utc)

	elaspedTime = utcManTime - utcEpochTime


	elaspedSeconds = ((elaspedTime.days * SECONDS) + elaspedTime.seconds)

	difference = utcManTime.second - utcEpochTime.second
	startDiff = interval + difference

# If not, use the current system time and calculate the elasped seconds
else:
	
	# Calculating the elasped time
	elaspedTime = curTime - epochTime

	elaspedSeconds = ((elaspedTime.days * SECONDS) + elaspedTime.seconds)

	# Calculating the difference
	difference = utcEpochTime.second - curTime.second
	startDiff = interval + difference

# Changing the elasped seconds to the start of the interval
correctedElasped = elaspedSeconds - startDiff

# Converting the number of seconds to a hash and then hashing the hash
firstMD5 = md5(str(correctedElasped))
secondMD5 = md5(firstMD5.hexdigest())

# Converts the hash to a hex string
strMD5 = str(secondMD5.hexdigest())

# Code to search through the hex string to find the first 2 letters and last 2 numbers
code = ""
i = 0
j = (len(strMD5)-1)
while (i < len(strMD5)):
	if (strMD5[i].isalpha()):
		code += strMD5[i]
	if (len(code) == 2):
		i = len(strMD5)
	i += 1
while (j > 0):
	if (strMD5[j].isdigit()):
		code += strMD5[j]
	if (len(code) == 4):
		j = 0
	j -= 1

code += strMD5[16]

if (DEBUG == True):
	print ("Current (UTC): "),
	print (utcManTime)
	print ("Epoch (UTC): "),
	print (utcEpochTime)
	print ("Seconds: "),
	print (elaspedSeconds)
	print ("Seconds: "),
	print (correctedElasped)
	print ("MD5 #1: " + firstMD5.hexdigest())
	print ("MD5 #2: " + secondMD5.hexdigest())

print code



