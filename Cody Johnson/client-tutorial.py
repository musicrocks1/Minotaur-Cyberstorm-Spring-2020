##python 2

import socket
from sys import stdout
from time import time
from binascii import unhexlify

# enables debugging output
DEBUG = False

# variable to hold binary covert message
covert_bin = ""

# set the server's IP address and port
ip = "138.47.99.163"
port = 12321

# create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server
s.connect((ip, port))

ZERO = 0.19
ONE = 0.09

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
	# calculate the time delta
	delta = round(t1 - t0, 3)
	# append 1 to binary message if delta >= 0.1 seconds, 0 if delta < 0.1 seconds
	if (delta >= ONE):
		covert_bin += "1"
	else:
		covert_bin += "0"
	if (DEBUG):
		stdout.write(" {}\n".format(delta))
		stdout.flush()

# close the connection to the server
s.close()

# variable to hold decoded binary message
covert = ""
i = 0

# decode each 8 bits of the binary message as a separate character
#     run until the binary message ends
while (i < len(covert_bin)):
	b = covert_bin[i:i + 8]
	n = int("0b{}".format(b), 2)
	# try to convert the decimal number in n to hex and then to ascii
	#     if it succeeds, append the converted character to covert
	#     if it fails, append a question mark instead
	try:
		covert += unhexlify("{0:x}".format(n))
	except TypeError:
		covert += "?"
	# go to the next byte
	i += 8

# print the hidden message
print "Hidden message: \"" + covert + "\""
