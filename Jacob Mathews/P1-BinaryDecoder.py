#####################################################################################
# Jacob Mathews
# Program 1 Binary Decoder
# 3/30/20
# Python Version 2.7
#####################################################################################
from sys import stdin
binary = stdin.read().rstrip("\n")
flip = True

# convert a string of zeros and ones using the ASCII table (n bits -> one ASCII value)
def decode(binary, n, m):
    global flip
    text = ""
    i = 0
    while (i<len(binary)):
        if(flip):
            byte = binary[i:i+n]    # look at sections of the binary based on parameter passed
        else:
            byte = binary[i:i+m]
        print byte


        byte = int(byte,2)      # convert to base 10

        if(byte == 8):          # special case when backspace is decoded
            text = text[:-1]    # returns the string without the last character

        else:                   # all other characters
            text+=chr(byte)

        if(flip):
            i+=n
        else:
            i+=m
        flip = not flip

    return text


##############
#    MAIN    #
##############

message = decode(binary, 7, 8)
print message
