############################################################################################
# Jacob Mathews
# Program 5: Timelock
# Python 2.7
# 5/8/20
############################################################################################
from sys import stdin
import datetime
import pytz
from hashlib import md5

# set True to see intermediate values
DEBUG = False

# interval for
INTERVAL = 60

# set to override use of system time
# format YYYY MM DD HH mm SS
MANUAL_DATETIME = ""

# get EPOCH_TIME from stdin
EPOCH_TIME = stdin.read().rstrip("\n")

# timezone variables for converstions
central = pytz.timezone('US/Central')
utc = pytz.timezone('UTC')

# if MANUAL_DATETIME is set properly, use it, if not use system time
# creates now datetime variable
if(len(MANUAL_DATETIME) == 19):
    now = [int(i) for i in (MANUAL_DATETIME.split())]
    now = datetime.datetime(now[0], now[1], now[2], now[3], now[4], now[5])
else:
    now = datetime.datetime.now()

# creates epoch datetime variable
epoch = [int(i) for i in (EPOCH_TIME.split())]
epoch = datetime.datetime(epoch[0], epoch[1], epoch[2], epoch[3], epoch[4], epoch[5])

# convert datetimes from central to utc to avoid daylight savings confusion
nowUtc = central.localize(now).astimezone(utc)
epochUtc = central.localize(epoch).astimezone(utc)

if(DEBUG):
    print "Current time UTC: ", nowUtc
    print "Epoch time UTC: ", epochUtc

# calculate number of seconds between now and epoch
elapsed = int((nowUtc-epochUtc).total_seconds())

if(DEBUG):
    print "Elapsed time: ", elapsed

# sets elapsed to the beginning of the INTERVAl
elapsed -= elapsed % INTERVAL

if(DEBUG):
    print "Elapsed time adjusted: ", elapsed

# apply the md5 hash twice
hashcode = md5(str(elapsed)).hexdigest()
hashcode = md5(str(hashcode)).hexdigest()

if(DEBUG):
    print "Hashcode: ", hashcode

# holds the desired code
code = ""

# add the first 2 leftmost letters to code
for char in hashcode:
    if(char.isalpha()):
        code += char
    if(len(code)>=2):
        break

# add the first two rightmost numbers to code
i = len(hashcode) - 1
while(i > 0):
    if(hashcode[i].isdigit()):
        code += hashcode[i]
    if(len(code) >= 4):
        break
    i-=1
code += hashcode[15:17]
print hashcode
print code
