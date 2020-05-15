###############################################################################################################################
# Name: Cullen Adams
# Date: 5/8/2020
# Assignment: Program 6: XOR Crypto
# Python Version: 2.7
###############################################################################################################################
from sys import stdin, stdout

# A variable to make changing what the key is easier
key = "key"

# This code tries to read the key, and tells the user to ensure that both files are in teh same directory if an error occurs.
try:
    keyFile = open(key, "r")
    keyBin = keyFile.read()
    keyFile.close()
except:
    print ("Uh oh! Make sure the key is in this directory!")

plain = stdin.read() # Uses stdin (standard input) to read user input (or a file using piping)

# This block does the xor cypher! I did some light googling and found some resources saying  ord is the best way to do this
message = ""
for character in range(len(plain)):
    counter = character % len(keyBin)
    plainCharacter = ord(plain[character])
    keyCharacter = ord(keyBin[counter])
    Character = plainCharacter ^ keyCharacter
    message += chr(Character)

stdout.write(message)