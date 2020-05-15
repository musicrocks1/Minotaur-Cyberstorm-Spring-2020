# Name: Joseph Siharath
# Due Date: MArch 30, 2020
# Description: This program takes in 7-bit or 8-bit binary and decodes it to readable text
from sys import stdin

# Decode function which takes the binary input and separates the binary to 7 or 8 bit 
# sections and then converts it to characters
def decode(binary, n):
	text = ""
	i = 0
	while (i < len(binary)):
		byte = binary[i:i+n]
		byte = int(byte, 2)
		if (byte == 8):
			text = text[:-1]
		else:
			text += chr(byte)
		i += n

	return text

# Takes in binary input from standard input(command line)
binary = stdin.read().rstrip("\n")

# Determines if it is 7 or 8 bit based on if it divides evenly and sends it to the 
# decode function
if (len(binary) % 7 == 0):
	text = decode(binary, 7)
	print "7-bit:"
	print text
if (len(binary) % 8 == 0):
	text = decode(binary, 8)
	print "8-bit"
	print text
	
