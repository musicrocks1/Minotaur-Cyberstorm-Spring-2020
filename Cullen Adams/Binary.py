####################################################################################################################################################
# Name : Cullen Adams
# Date: 3/28/2020
# Assignment: Program 1: Binary Decoder
# Python Version: 2
####################################################################################################################################################
from sys import stdin # Imports stdin from the sys (system) library

def decode(binary, n):
    text = "" # Creates an empty string to add (or in the case of Backspace, subtract) characters from after they are decoded
    i = 0 # Simple counter to see if we have reached the end of the binary string
    while (i < len(binary)):
        byte = binary[i:i+n] # Stores one byte of size n in byte, starting at id
        byte = int(byte, 2) # Converts the n bit byte into decimal
        if (byte == 8): # If the character is a Backspace:
            text = text[:-1] # Remove the last character of the text
        else:
            text += chr(byte) # Add the decrypted (using a function included in python) character on to the text
        i += n # Iterate the counter
    return text # When the while condition has been broken, return the decoded text!

binary = stdin.read().rstrip("\n") # Uses stdin (standard input) to read user input (or a file using piping), and removes a new line from the end

if(len(binary) % 7 == 0): # If the text is encoded in 7-bit binary, decode it using 7 bits to a byte
    text = decode(binary, 7)
    print("7-bit:")
    print(text)
if(len(binary) % 8 == 0): # If the text is encoded in 8-bit binary, decode it using 8 bits to a byte
    text = decode(binary, 8)
    print("8-bit:")
    print(text)
