#################
# Jonah Landry
# Python 3
# XOR En/Decoder
# 5/8/2020
#################

#Imports
import sys

#Variables
#By opening the key as rb, we open it in binary read.
keyBin = open("key", "rb")
key = keyBin.read()
byteKey = bytearray(key)

#Get the file from stdin and convert it to a bytearray
binInput = sys.stdin.buffer.read()
byteIn = bytearray(binInput)

#Functions
#Takes a given text and a given key already translated to bytearrays
# and returns the result of an XOR operation converted to ascii and
# appended to a string
def byteXOR(text, key):
    counter = 0
    output = ""
    while counter < len(byteIn):
        temp = text[counter] ^ key[counter%len(key)]
        output = output + (chr(temp))
        counter = counter + 1
    return output


#Gets the array by sending inputs to byteXOR and printing them
finalArray = byteXOR(byteIn, byteKey)
print(finalArray)

