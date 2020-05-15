#########################################################################################################
# Name: Cullen Adams
# Date: 4/23/20
# Assignment: Program #4: Chat (timing) covert channel
# Python version: 2.7
#########################################################################################################

import socket
from sys import stdout
from time import time

# A function from an old assignment, used to decode the covert message.
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

# enables debugging output. If the message seems to break, put on debug and check to see if the timing is out of range through the garbled text
DEBUG = True

# set the server's IP address and port, and set a variable to keep the current covert and decoded covert message in, as well as a variable to keep track of if the covert message has ended. Also have two variables for the timing delay for a 0 and for a 1.
ip = "138.47.102.67"
port = 33333
covert = ""
decovert = ""
check = 0
final = ""

# create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server
s.connect((ip, port))

# receive data until EOF
data = s.recv(4096)
while (data.rstrip("\n") != "EOF"):
	# output the data
	stdout.write(data)
	stdout.flush()
	# start the "timer", get more data, and end the "timer"
	t0 = time()
	data = s.recv(4096)
	t1 = time()
	# calculate the time delta (and output if debugging)
	delta = round(t1 - t0, 3)
	# After using one of the debug lines to determine timing, figure out if the delay is a 0 or 1. Also, the timing was slightly inconsistent, so I implemented a small range of error.
	if (delta > .04 and delta <= .15):
		covert += '0'
	elif (delta > .151 and delta < .25):
		covert += '1'
	# Decode using whichever byte size might work (assuming the final message is not decoded)
	if ((len(covert) % 7 == 0) and (check == 0)):
		decovert = decode(covert, 7)
	if ((len(covert) % 8 == 0) and (check == 0)):
		decovert = decode(covert, 8)
	# If the full message has been decoded, stop changing the message!
	if (decovert[-3:] == "EOF"):
		check = 1
		decovert = decovert[:-3]
		final = decovert
	# Depending on which line is commented out, either prints the decoded message or the timing next to each character
	if (DEBUG):
		stdout.write(" {}\n".format(decovert))
		stdout.write(" {}\n".format(delta))
		stdout.flush()

# close the connection to the server and print the decoded covert message
s.close()
print
if (final != ""): 
	print "Covert message: " + final
else:
	print "Hmm... I didn't detect a message. Try again?"
