# python 3

from sys import stdin
from datetime import datetime
from pytz import timezone
from hashlib import md5


# variables to be changed
DEBUG = False
interval = 60
finalTime = ""


# read epoch time from stdin
startTime = input()


# calculate current time in UTC if not given, otherwise
#     format given time as datetime and convert to UTC
if (finalTime == ""):
    finalTime = datetime.now(timezone("UTC"))
else:
    finalTime = datetime.strptime(finalTime, "%Y %m %d %H %M %S")
    finalTime = finalTime.astimezone(timezone("UTC"))
if (DEBUG):
    print("Current ({}): {}".format("UTC", finalTime))


# format epoch time as datetime and convert to UTC
startTime = datetime.strptime(startTime, "%Y %m %d %H %M %S")
startTime = startTime.astimezone(timezone("UTC"))
if (DEBUG):
    print("Epoch ({}): {}".format("UTC", startTime))


# calculate real number of seconds between both datetimes
realSeconds = (int)((finalTime - startTime).total_seconds())
if (DEBUG):
    print("Actual seconds: {}".format(realSeconds))


# calculate number of seconds according to interval
intervalSeconds = realSeconds - realSeconds % interval
if (DEBUG):
    print("Interval seconds: {}".format(intervalSeconds))


# get first MD5 hash
myFirstMd5 = md5(str(intervalSeconds).encode("utf-8")).hexdigest()
if (DEBUG):
    print("MD5 #1: {}".format(myFirstMd5))


# get second MD5 hash
mySecondMd5 = md5(myFirstMd5.encode("utf-8")).hexdigest()
if (DEBUG):
    print("MD5 #2: {}".format(mySecondMd5))


# get code from first two letters from left to right, and
#     first two numbers from right to left
code = ""
# get two letters from left to right
for i in range(len(mySecondMd5)):
    if (len(code) < 2):
        if (ord(mySecondMd5[i]) >= 97 and ord(mySecondMd5[i]) <= 102):
            code += mySecondMd5[i]
    else:
        break
# get two numbers from right to left
for i in range(len(mySecondMd5) - 1, -1, -1):
    if (len(code) < 4):
        if (ord(mySecondMd5[i]) >= 48 and ord(mySecondMd5[i]) <= 57):
            code += mySecondMd5[i]
    else:
        break
# get middle two numbers
code += mySecondMd5[len(mySecondMd5) // 2 - 1]
code += mySecondMd5[len(mySecondMd5) // 2]
if (DEBUG):
    print("Code: {}".format(code))
else:
    print(code)
