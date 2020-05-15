###############################################################################
# Jacob Mathews
# Program 7 Steg
# 5/8/20
# Python Version 2.7
###############################################################################
from sys import argv
# will be appended to hidden data
SENTINEL = [0x0,0xff,0x0,0x0,0xff,0x0]

def main():
    # input variables
    mode = argv[1]
    method = argv[2]
    offsetVal = 0
    intervalVal = 1
    wrapperFile = ""
    hiddenFile = ""

    # parses remaining input parameters with some error handling
    i=3
    while(i<len(argv)):
        if(argv[i][:2] == "-o"):
            offsetVal = int(argv[i][2:])
        elif(argv[i][:2] == "-i"):
            intervalVal = int(argv[i][2:])
        elif(argv[i][:2] == "-w"):
            try:
                w = open(argv[i][2:])
            except IOError:
                print "ERROR: wrapper file not found"
                exit(0)
            wrapperFile = w.read()
            w.close()
            wrapperFile = bytearray(wrapperFile)
        elif(argv[i][:2] == "-h"):
            try:
                h = open(argv[i][2:])
            except IOError:
                print "ERROR: hidden file not found"
                exit(0)
            hiddenFile = h.read()
            h.close()
            hiddenFile = bytearray(hiddenFile)
        else:
            print "ERROR INVALID PARAMETERS."
            print "Please follow the form of:"
            print "python P7-Steg.py -(sr) -(bB) -o<val> [-i<val>] -w<val> [-h<val>]"
            exit(0)
        i+=1

    # calls proper function based on parameters
    if(mode == "-s" and method == "-B"):
        if(wrapperFile == ""):
            print "ERROR: no wrapper file"
            exit(0)
        if(hiddenFile == ""):
            print  "ERROR: no hidden file"
            exit(0)
        else:
            byteStore(offsetVal, intervalVal, wrapperFile, hiddenFile)
    elif(mode == "-s" and method == "-b"):
        if(wrapperFile == ""):
            print "ERROR: no wrapper file"
            exit(0)
        if(hiddenFile == ""):
            print  "ERROR: no hidden file"
            exit(0)
        else:
            bitStore(offsetVal, intervalVal, wrapperFile, hiddenFile)
    elif(mode == "-r" and method == "-B"):
        if(wrapperFile == ""):
            print "ERROR: no wrapper file"
            exit(0)
        else:
            byteRetrieve(offsetVal, intervalVal, wrapperFile)
    elif(mode == "-r" and method == "-b"):
        if(wrapperFile == ""):
            print "ERROR: no wrapper file"
            exit(0)
        else:
            bitRetrieve(offsetVal, intervalVal, wrapperFile)
    else:
        print "ERROR INVALID PARAMETERS."
        print "-(sr) and -(bB) are required parameters"
        exit(0)

## replaces every interval'th byte of the wrapperBytes with the next hiddenBytes
## or SENTINEL byte until complete
def byteStore(offset, interval, wrapperBytes, hiddenBytes):
    i = 0
    while(i < len(hiddenBytes)):
        try:
            wrapperBytes[offset] = hiddenBytes[i]
        except IndexError:
            print "ERROR: wrapper file is not big enough"
            exit(0)

        offset += interval
        i+=1

    i = 0
    while(i < len(SENTINEL)):
        wrapperBytes[offset] = SENTINEL[i]
        offset += interval
        i+=1

    newWrapper = ""
    for byte in wrapperBytes:
        newWrapper += chr(byte)
    print newWrapper

# replaces the least signifcant bit of the interval'th byte of the wrapperBytes
# with the next hiddenBytes or SENTINEL bit until complete
def bitStore(offset, interval, wrapperBytes, hiddenBytes):
    i = 0
    while(i < len(hiddenBytes)):
        for j in range(8):
            try:
                wrapperBytes[offset] &= (0xfe)
            except IndexError:
                print "ERROR: wrapper file is not big enough"
                exit(0)
            wrapperBytes[offset] |= ((hiddenBytes[i] & 0x80) >> 7)
            hiddenBytes[i] = (hiddenBytes[i] << 1) & 0xff
            offset += interval
        i+=1
    i = 0
    while(i < len(SENTINEL)):
        for j in range(8):
            wrapperBytes[offset] &= (0xfe)
            wrapperBytes[offset] |= ((SENTINEL[i] & 0x80) >> 7)
            SENTINEL[i] = (SENTINEL[i] << 1) & 0xff
            offset += interval
        i+=1


    newWrapper = ""
    for byte in wrapperBytes:
        newWrapper += chr(byte)
    print newWrapper

## stores every interval'th byte of wrapperBytes until the six SENTINEL bytes
## are found then outputs the stored bytes without SENTINEL bytes
def byteRetrieve(offset, interval, wrapperBytes):
    global SENTINEL
    hiddenBytes = []
    while(offset < len(wrapperBytes)):
        b = wrapperBytes[offset]
        hiddenBytes.append(b)
        offset += interval

        if(hiddenBytes[-6:] == SENTINEL):
            hiddenBytes = hiddenBytes[:-6]
            break

    hidden = ""
    for byte in hiddenBytes:
        hidden += chr(byte)
    print hidden

## stores the least signifcant bit of the interval'th byte of wrapperBytes until the
## six SENTINEL bytes are found, then outputs the stored bytes without the SENTINEL bytes
def bitRetrieve(offset, interval, wrapperBytes):
    hiddenBytes = []
    while(offset < len(wrapperBytes)):
        b = 0
        for j in range(8):
            try:
                b |= (wrapperBytes[offset] & 0x01)
            except IndexError:
                print "ERROR. Sentinel bytes not found."
                exit(0)
            if(j < 7):
                b = (b << 1) & (0xff)
                offset += interval

        hiddenBytes.append(b)

        if(hiddenBytes[-6:] == SENTINEL):
            hiddenBytes = hiddenBytes[:-6]
            break
        offset += interval

    hidden = ""
    for byte in hiddenBytes:
        hidden += chr(byte)
    print hidden

#############
#   MAIN    #
#############
main()
