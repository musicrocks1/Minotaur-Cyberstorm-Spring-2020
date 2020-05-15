###############################################################################################################################
# Name: Cullen Adams
# Date: 5/7/2020
# Assignment: Program 7: Steg
# Python Version: 2.7
###############################################################################################################################
from sys import stdin, stdout, argv, exit

DEBUG = False
STORE = False
RETREIVE = False
BITMODE = False
BYTEMODE = False
OFFSET = 0
INTERVAL = 1
WFILE = ""
HFILE = ""
SENTINEL = bytearray([0x0, 0xff, 0x0, 0x0, 0xff, 0x0])

'''def Wrong():
    print "Incorrect usage! Try with correct usage: \"python Steg.py -(sr) -(bB) -o<val> [-i<val>] -w<val> [-h<val>]\""
    print "Here are two examples of correct usage! \"python Steg.py -s -B -o1024 -i256 -wimage.jpg -hsecret.jpg > new.jpg\""
    print "\"python Steg.py -r -B -o1024 -i256 -wnew.jpg > extracted.jpg\""
    exit()'''

# This begins the lengthy parameter check section, where I make sure the person using the program knows how to use it.
# I also set the variables from earlier to be True depending on what the user inputs.
for parameter in argv:
    if (parameter == "-s"):
        STORE = True
    if (parameter == "-r"):
        RETREIVE = True
    if (parameter == "-b"):
        BITMODE = True
    if (parameter == "-B"):
        BYTEMODE = True
    if (parameter[:2] == "-o"):
        if(len(parameter) > 2):
            OFFSET = int(parameter[2:])
    if (parameter[:2] == "-i"):
        if(len(parameter) > 2):
            INTERVAL = int(parameter[2:])
    if (parameter[:2] == "-w"):
        if(len(parameter) > 2):
            WFILE = str(parameter[2:])
    if (parameter[:2] == "-h"):
        if(len(parameter) > 2):
            HFILE = str(parameter[2:])

# Simple debug here to check the values of all of the important variables.
if (DEBUG):
    print "STORE is " + str(STORE)
    print "RETREIVE is " + str(RETREIVE)
    print "BITMODE is " + str(BITMODE)
    print "BYTEMODE is " + str(BYTEMODE)
    print "OFFSET is " + str(OFFSET)
    print "INTERVAL is " + str(INTERVAL)
    print "WFILE is " + WFILE
    print "HFILE is " + HFILE

# These two blocks of code read the specified files and convert their data to binary, assuming they're in the same folder as
# this file. If not, it prints out a fun error message for the user. Yay!
if (WFILE != ""):
    try:
        wfile = open(WFILE, "rb")
        wbin = bytearray(wfile.read())
    except:
        print ("Uh oh! Make sure that the wrapper file you are trying to use is in the same directory as Steg.py!")

if (HFILE != ""):
    try:
        hfile = open(HFILE, "rb")
        hbin = bytearray(hfile.read())
    except:
        print ("Uh oh! Make sure that the hidden file you are trying to use is in the same directory as Steg.py!")

if (STORE):
    i = 0
    while (i < len(hbin)):
        # This try except block handles an error that throws when the wrapper file is too small for the selected interval.
        try:
            wbin[OFFSET] = hbin[i]
            OFFSET += INTERVAL
            i += 1
        except IndexError:
            print "Your wrapper file is most likely too small for the selected interval. Either lower the interval or use a bigger file!"
            exit()

    i = 0
    while(i < len(SENTINEL)):
        wbin[OFFSET] = SENTINEL[i]
        OFFSET += INTERVAL
        i += 1
    stdout.write(wbin)

if (RETREIVE):
    H = bytearray()
    maybeSentinel = bytearray()
    while (OFFSET < len(wbin)):
        b = wbin[OFFSET]
        if (b == SENTINEL[0]):
            i = 0
            for byte in SENTINEL:
                i += 1
                maybeSentinel.append(b)
                temp = wbin[OFFSET + INTERVAL]
                if (temp != SENTINEL[i]):
                    break
                elif (maybeSentinel == SENTINEL):
                    stdout.write(H)
                    exit()
        H.append(b)
        OFFSET += INTERVAL
    stdout.write(H)
    