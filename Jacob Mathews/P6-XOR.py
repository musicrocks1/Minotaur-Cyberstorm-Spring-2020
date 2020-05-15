#####################################################################################
# Jacob Mathews
# Program 2 XOR
# 5/8/20
# Python Version 2.7
#####################################################################################
from sys import stdin
# set true to see intermediate values
DEBUG = False

# get key data from a file named key in current directory
f = open("key")
key = f.read()
f.close()

# get input message data from standard input
input = stdin.read()

# convert key and input into binary data
key = bytearray(key)
input = bytearray(input)

# if the key is too short, repeat the key until it is long enough
i = 0
while(len(input) > len(key)):
    key.append(key[i])
    i+=1

# if the key is too long, truncate the key to the correct length
while(len(input) < len(key)):
    key.pop()

# convert key and input data into one long string of bytes each
keyBin = ""
inputBin = ""
for j in range(len(input)):
    keyBin += str(bin(key[j]))[2:].zfill(8)
    inputBin += str(bin(input[j]))[2:].zfill(8)

if(DEBUG):
    print keyBin, "\n"
    print inputBin

# XOR the key and input together
outputBin = bin(int(keyBin, 2) ^ int(inputBin, 2))[2:].zfill(len(keyBin))

if(DEBUG):
    print "\n\n",outputBin

# seperate the XORed message into bytes and convert each byte into ASCII characters

outputText = ""
k = 0
while (k < len(outputBin)):
    outputText += chr(int(outputBin[k:k+8],2))
    
    k+=8

print outputText
