#########################################
from sys import stdin
# Jonah Landry
# Assignment 1
# Python 3
# Due 4/1/2020
########################################



def decode(binary,n): # binary = binary to be decoded n = the bit type (8 or 7)
    text = ""
    i = 0
    while (i < len(binary)):
        byte = binary[i:i+n]
        byte = int(byte,2)
        if (chr(byte) == "\b"):
            text = text[:-1]
        else:
            text += chr(byte)
        i += n

    return text

binary = stdin.read().rstrip("\n")

if (len(binary)%7 == 0):
    text = decode(binary,7)
    print ("7-bit:")
    print (text)
if (len(binary)%8 == 0):
    text = decode(binary,8)
    print ("8-bit")
    print (text)