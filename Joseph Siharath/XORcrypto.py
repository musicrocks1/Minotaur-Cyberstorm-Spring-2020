# Name: Joseph Siharath
# Due Date: 5/8/20
# Description: This program takes in a key and XOR the text to encrypt/decrypt using the key

# NOTE: This uses program python2.7

from sys import stdin, stdout

# File name MUST be in same folder
keyFile = "IRS.png"

# Get the text from stdin
givenText = bytearray(stdin.read())

# Read the file key and input the contents to a byte array
with open(keyFile, 'r') as f:
	key = bytearray(f.read())


# Create a byte array of the same size as the input text
text = bytearray(len(givenText))

# XOR each byte of the given with the key and append the text array
i = 0
j = 0
while (i < len(givenText)):
	text[i] = key[i] ^ givenText[i]
	i += 1
	j += 1

stdout.write(text)
