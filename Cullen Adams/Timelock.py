###############################################################################################################################
# Name: Cullen Adams
# Date: 5/7/2020
# Assignment: Program 5: TimeLock
# Python Version: 2.7
###############################################################################################################################
from sys import stdin
import pytz, datetime
from hashlib import md5

DEBUG = False

# All of the important constants (and a couple that we may need to change)
INTERVAL = 60
MANUAL_DATETIME = "2017 04 26 15 14 30"
ALPHABET = "abcdef"
NUMBERS = "1234567890"

# Converts MANUAL_DATETIME to UTC, because time zones and daylight's saving time suck.
local = pytz.timezone("America/Chicago")
MANUAL_DATETIME = datetime.datetime.strptime(MANUAL_DATETIME, "%Y %m %d %H %M %S")
MANUAL_DATETIME = local.localize(MANUAL_DATETIME, is_dst=None)
MANUAL_DATETIME = MANUAL_DATETIME.astimezone(pytz.utc)

# Converts epoch to UTC, because time zones and daylight's saving time suck.
epoch = stdin.read().rstrip("\n")
epoch = datetime.datetime.strptime(epoch, "%Y %m %d %H %M %S")
epoch = local.localize(epoch, is_dst=None)
epoch = epoch.astimezone(pytz.utc)

# Calculate the amount of seconds that have passed since the epoch, round it down to the nearest multiple 
# of the interval, get a md5 hash of the rounded amount of seconds, and get a md5 hash of that hash.
seconds = int((MANUAL_DATETIME-epoch).total_seconds())
roundedSeconds = int((MANUAL_DATETIME-epoch).total_seconds()) - int((MANUAL_DATETIME-epoch).total_seconds()) % INTERVAL
hash1 = md5(str(roundedSeconds)).hexdigest()
hash2 = md5(hash1).hexdigest()

# A useful debug to see all of the important things
if (DEBUG):
	print "Current (UTC): " + str(MANUAL_DATETIME)
	print "Epoch (UTC): " + str(epoch)
	print "Seconds: " + str(seconds)
	print "Seconds: " + str(roundedSeconds)
	print "MD5 #1: " + hash1
	print "MD5 #2: " + hash2

# This block of code steps through the hash, and adds the first two letters that it
# finds to a string called letters to be used later
letters = ""
for i in range(len(hash2)):
	for letter in ALPHABET:
		if hash2[i] == letter:
			letters += hash2[i]
		if len(letters) == 2:
			break
	if len(letters) == 2:
		break

# This block of code steps backwards through the hash, and adds the first two single digit integers it 
# finds to a string called numbers to be used later
numbers = ""
for i in xrange(len(hash2) - 1, 0, -1):
	for number in NUMBERS:
		if hash2[i] == number:
			numbers += hash2[i]
		if len(numbers) == 2:
			break
	if len(numbers) == 2:
		break

# If you couldn't guess, this prints the final code!
if (DEBUG):
	print "Code : " + letters + numbers
else:
	print letters + numbers
	
