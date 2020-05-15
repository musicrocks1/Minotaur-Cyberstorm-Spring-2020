# Name: Joseph Siharath
# Due Date: 4/24/20
# Description: This program reads a message from a chat channel that has a hidden message embedded in the delays and then decrypts the message

# Libraries
import socket
from sys import stdout
from time import time
from binascii import unhexlify

# enables debugging output
DEBUG = False

# set the server's IP address and port
ip = "localhost"
port = 1338

# create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server
s.connect((ip, port))

# Initializing strings
covertBin = ""
covert = ""

# Constants
ZERO = 0.025
ONE = 0.1

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

	# Debug to determine the delay timing 
	if (DEBUG):
		stdout.write(" {}\n".format(delta))
		stdout.flush()

	# Converts the hidden message into binary assuming the constants are correct
	if (delta >= ONE):
		covertBin += "1"
	else:
		covertBin += "0"

# Converts every 8 bits in the binary string to a character and then adds it to another string
i = 0
while (i < len(covertBin)):
	b = covertBin[i:i + 8]
	n = int("0b{}".format(b), 2)
	try:
		covert += unhexlify("{0:x}".format(n))
	except TypeError:
		covert += "?"
	i += 8
	

# close the connection to the server
s.close()

# Print the hidden message
print ("Hidden Message: " + covert)

