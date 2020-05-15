import socket
import time
from binascii import hexlify
# set the port for client connections
port = 1338

# create the socket and bind it to the port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", port))

# listen for clients
# this is a blocking call
s.listen(0)

# a client has connected!
c, addr = s.accept()

# Constants
ZERO = 0.025
ONE = 0.1

# set the message
msg = "Some Message that is being sent to the client. \n"

covert = "Secret Message" + "EOF"
covertBin = ""
for i in covert:
	covertBin += bin(int(hexlify(i), 16))[2:].zfill(8)
# send the message, one letter at a time
n = 0
for i in msg:
	c.send(i)
	if (covertBin[n] == "0"):
		time.sleep(ZERO)
	else:
		time.sleep(ONE)
	n = (n + 1) % len(covertBin)


# send EOF and close the connection to the client
c.send("EOF")
c.close()

