# python 3

from sys import stdin, stdout, argv


# variables for showing debug text and changing sentinel's value
DEBUG = False
SENTINEL = bytearray([0x0, 0xff, 0x0, 0x0, 0xff, 0x0])


# default values for offset, interval, and hidden variables
offset = 0
interval = 1
hidden = None


# try to read arguments in properly
# error if the order is incorrect, or required arguments are not provided
try:
    # read action (-s/-r) in
    if (argv[1][0:2] == "-s" or argv[1][0:2] == "-r"):
        action = argv[1]
    else:
        raise
    if (DEBUG):
        print("action: {}".format(action))
        
    # read mode (-b/-B) in
    if (argv[2][0:2] == "-b" or argv[2][0:2] == "-B"):
        mode = argv[2]
    else:
        raise
    if (DEBUG):
        print("mode: {}".format(mode))
        
    # read offset (-o) in
    if (argv[3][0:2] == "-o" and len(argv[3]) > 2):
        offset = int(argv[3][2:len(argv[3])])
    else:
        raise
    if (DEBUG):
        print("offset: {}".format(offset))
        
    # read interval (-i) in if provided
    count = 4
    if (argv[4][0:2] == "-i"):
        if (len(argv[4]) <= 2):
            raise
        interval = int(argv[4][2:len(argv[4])])
        count += 1
    if (DEBUG):
        print("interval: {}".format(interval))
        
    # read wrapper (-w) in
    if (argv[count][0:2] == "-w" and len(argv[count]) > 2):
        wrapper = argv[count][2:len(argv[count])]
    else:
        raise
    if (DEBUG):
        print("wrapper: {}".format(wrapper))
        
    # read hidden (-h) in if provided
    count += 1
    if (len(argv) > count and argv[count][0:2] == "-h"):
        if (len(argv[count]) <= 2):
            raise
        hidden = argv[count][2:len(argv[count])]
    if (DEBUG):
        print("hidden: {}".format(hidden))
        
# print error message if there was a problem with the arguments
except:
    print("An error occurred. Please make sure your command is in the following format:")
    print("    python steg.py -(sr) -(bB) -o<val> [-i<val>] -w<val> [-h<val>]")
    exit()


# try to open the wrapper file, and error if it fails
# read its contents into wrapperContents as bytearray
try:
    with open(wrapper, "rb") as myfile:
        wrapperContents = bytearray(myfile.read())
except:
    print("Error: File to wrap does not exist in current directory.")
    exit()


# if the hidden file is being stored in the wrapper
if (action == "-s"):
    # try to open the binary file hidden, and error if it does not exist
    # read its contents into hiddenContents as bytearray
    try:
        with open(hidden, "rb") as myfile:
            hiddenContents = bytearray(myfile.read())
    except:
        print("Error: File to hide does not exist in current directory.")
        exit()

    # if using the LSB of each wrapper byte to store a single hidden bit
    if (mode == "-b"):
        # store the first bit of the hidden byte in the LSB of a wrapper byte, then
        #     go to the next wrapper byte and store the next bit of the hidden byte in its LSB
        # repeat until the entire hidden byte has been stored, then
        #     move on to the next hidden byte
        # repeat until the entire hidden message has been stored
        i = 0
        while i < len(hiddenContents):
            for j in range(8):
                wrapperContents[offset] &= 0b11111110
                wrapperContents[offset] |= ((hiddenContents[i] & 0b10000000) >> 7)
                hiddenContents[i] = (hiddenContents[i] << 1) & (2 ** 8 - 1)
                offset += interval

            i += 1

        # store the first bit of the sentinel byte in the LSB of a wrapper byte, then
        #     go to the next wrapper byte and store the next bit of the sentinel byte in its LSB
        # repeat until the entire sentinel byte has been stored, then
        #     move on to the next sentinel byte
        # repeat until the entire sentinel has been stored
        i = 0
        while i < len(SENTINEL):
            for j in range(8):
                wrapperContents[offset] &= 0b11111110
                wrapperContents[offset] |= ((SENTINEL[i] & 0b10000000) >> 7)
                SENTINEL[i] = (SENTINEL[i] << 1) & (2 ** 8 - 1)
                offset += interval

            i += 1

    # if using an entire wrapper byte to store a hidden byte
    elif (mode == "-B"):
        # replace the wrapper byte with the hidden byte, then
        #     go to next wrapper byte and repeat until hidden message is stored
        i = 0
        while i < len(hiddenContents):
            wrapperContents[offset] = hiddenContents[i]
            offset += interval
            i += 1
            if (DEBUG):
                print("hidden content byte added at offset = {}".format(offset))

        # replace the wrapper byte with the sentinel byte, then
        #     go to next wrapper byte and repeat until sentinel is stored
        i = 0
        while i < len(SENTINEL):
            wrapperContents[offset] = SENTINEL[i]
            offset += interval
            i += 1
            if (DEBUG):
                print("sentinel byte added at offset = {}".format(offset))

    # send output to stdout
    if (DEBUG):
        print("writing output to file...")
    stdout.buffer.write(wrapperContents)

# if the hidden file is being retrieved from the wrapper
elif (action == "-r"):
    hiddenContents = bytearray()

    # if retrieving a single hidden bit from the LSB of each wrapper byte
    if (mode == "-b"):
        count = 0
        temp = bytearray()
        while offset < len(wrapperContents):
            b = 0
            # get entire hidden byte
            for j in range(8):
                b |= (wrapperContents[offset] & 0b00000001)
                if (j < 7):
                    b = (b << 1) & (2 ** 8 - 1)
                    offset += interval
            # check if hidden byte is the first sentinel byte
            # if so, store it in temp instead and continue
            if (b == SENTINEL[count]):
                if (DEBUG):
                    print("bytes found equal ({}), count = {}, offset = {}".format(b, count, offset))
                # if all sentinel bytes are found, break
                if (count >= len(SENTINEL) - 1):
                    if (DEBUG):
                        print("breaking early...")
                    break
                count += 1
                temp.append(b)
                offset += interval
                continue
            # if a later byte is found to be not in sentinel, then
            #     append temp bytes to end of hidden bytes and keep going
            elif (count > 0):
                if (DEBUG):
                    print("bytes no longer equal ({} vs {}), count = {}, offset = {}".format(b, SENTINEL[count], count, offset))
                count = 0
                for t in temp:
                    hiddenContents.append(t)
                temp = bytearray()
            hiddenContents.append(b)
            offset += interval

    # if retrieving a hidden byte from the entire wrapper byte
    elif (mode == "-B"):
        count = 0
        temp = bytearray()
        while offset < len(wrapperContents):
            # get hidden byte
            b = wrapperContents[offset]
            # check if hidden byte is the first sentinel byte
            # if so, store it in temp instead and continue
            if (b == SENTINEL[count]):
                if (DEBUG):
                    print("bytes found equal ({}), count = {}, offset = {}".format(b, count, offset))
                # if all sentinel bytes are found, break
                if (count >= len(SENTINEL) - 1):
                    if (DEBUG):
                        print("breaking early...")
                    break
                count += 1
                temp.append(b)
                offset += interval
                continue
            # if a later byte is found to be not in sentinel, then
            #     append temp bytes to end of hidden bytes and keep going
            elif (count > 0):
                if (DEBUG):
                    print("bytes no longer equal ({} vs {}), count = {}, offset = {}".format(b, SENTINEL[count], count, offset))
                count = 0
                for t in temp:
                    hiddenContents.append(t)
                temp = bytearray()
            hiddenContents.append(b)
            offset += interval

    # send output to stdout
    if (DEBUG):
        print("writing output to file...")
    stdout.buffer.write(hiddenContents)
