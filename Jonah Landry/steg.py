######################
# Jonah Landry
# STEG
# 5/8/2020
# Python 3
######################

# Steg is the idea of hiding something in something else. This program finds that something
# imports

#Used for taking commands from commandline
import sys

sent = bytearray([0, 255, 0 , 0, 255, 0])

#Stop reading when the next six bytes are 0x0 0xff 0x0 0x0 0xff 0x0

#Byte method which replaces a whole byte in the file
#Byte storage
def byteStore(wrapper, hidden, offset, interval):
    i = 0
    while i < len(hidden):
        wrapper[offset] = hidden[i]
        offset = offset + 1
        i = i + 1

    i = 0
    while i < len(sent):
        wrapper[offset] = sent[i]
        offset = offset + interval
        i = i + 1

    return wrapper

#Byte reading
def byteRead(wrapper,  offset, interval):
    hidden = bytearray()
    CurrBytes = bytearray()
    i = 0
    while offset < len(wrapper):
        CurrBytes.append(wrapper[offset])
        if (CurrBytes[i] == sent[i]):
            i = i + 1
            if i >= len(sent):
                offset = len(wrapper) #If we find the stop we stop
        else:
            for CurrByte in CurrBytes:
                hidden.append(CurrByte)
            i = 0 #Resets doomsday counter
            CurrBytes = bytearray() #clears CurrBytes
        offset = offset + interval
    return hidden

#Bit storage
def bitStore(wrapper, hidden, offset, interval):
    i = 0
    while i < len(hidden):
        for j in range(8):
            wrapper[offset] &= 0o11111110
            wrapper[offset] |= ((H[i] & 0o1000000) >> 7)
            hidden[i] = (hidden[i] << 1) & (2 ** 8 - 1)
            offset = offset + interval
        i = i + 1
    i = 0
    while i < len(sent):
        for j in range(8):
            wrapper[offset] &= 0o11111110
            wrapper[offset] |= ((sent[i] & 0o10000000) >> 7)
            sent[i] = (sent[i] << 1) & (2 ** 8 - 1)
            offset += interval
        i = i + 1
    return wrapper

#Byte reading
def bitRead(wrapper, offset, interval):
    i = 0
    hidden = bytearray()
    tempArray = bytearray()
    while offset < len(wrapper):
        b = 0
        #Gets us our bytey boy
        for j in range(8):
            b = b | (wrapper[offset] & 0o00000001)
            if j < 7:
                b = (b << 1) & (2 ** 8 - 1)
                offset = offset + interval
        tempArray.append(b)

        # Look for sentinel bytes
        if (tempArray[i] == sent[i]):
            i = i + 1
            if i >= len(sent):
                offset = len(wrapper)
        else:
            for tempByte in tempArray:
                hidden.append(tempByte)
            i = 0
            tempArray = bytearray()
        offset = offset + interval
    return hidden





#Bit method spreads the hidden bytes into the last slot of each wrapper byte.


#Sets arguments to more understandable values. Initializes flags to record whats missing for
#debug

missingFlags = ["storage", "mode", "offset", "interval", "wrapper", "hidden"]
interval = 1
arguments = sys.argv[1:]
for argument in arguments:
    if (argument == "-s" or argument == "-r"):
        storageMode = argument
        missingFlags[0] = " "
    elif (argument == "-b" or argument == "-B"):
        mode = argument
        missingFlags[1] = " "
    elif (argument[:2] == "-o"):
        offset = int(argument[2:])
        missingFlags[2] = " "
    elif (argument[:2] == "-i"):
        interval = int(argument[2:])
        missingFlags[3] = " "
    elif (argument[:2] == "-w"):
        wrapper = argument[2:]
        try:
            wrapperFile = open(wrapper, "rb")
            wrapB = bytearray(wrapperFile.read())
        except:
            sys.stdout.write("FILE NOT FOUND")
            sys.stdout.flush()
            exit()
        missingFlags[4] = " "
    elif (argument[:2] == "-h"):
        hidden = argument[2:]
        try:
            hiddenFile = open(hidden, "rb")
            hiddenB = bytearray(hiddenFile.read())
        except:
            sys.stdout.write("FILE NOT FOUND")
            sys.stdout.flush()
            exit()
        missingFlags[5] = " "

newB = ""
#Parses the arguments to perform the proper function
if (arguments[0] == "-s"):
    if(arguments[1] == "-b"):
        newB = bitStore(wrapB, hiddenB, offset, interval)
    if(arguments[1] == "-B"):
        newB = byteStore(wrapB, hiddenB, offset, interval)
elif (arguments[0] == "-r"):
    if(arguments[1] == "-b"):
        newB = bitRead(wrapB, offset, interval)
    if(arguments[1] == "-B"):
        newB = byteRead(wrapB, offset, interval)


sys.stdout.buffer.write(newB)

