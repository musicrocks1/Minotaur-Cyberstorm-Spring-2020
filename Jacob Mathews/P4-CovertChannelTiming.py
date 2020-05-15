import socket
from sys import stdout
from time import time
from binascii import unhexlify

# set the server's IP address and port
ip = "138.47.99.163"
port = 12321
# create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect to the server
s.connect((ip, port))

# 1 for debug mode otherwise 0
DEBUG = 0

# timing constants
ZERO = .1
ONE = .2
IGNORE = .15

# message variables
covertBin = ""
covert = ""

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

    # gather binary covert message using timing
    delta = round(t1 - t0, 3)
    if(DEBUG):
        stdout.write("\nDELTA: " + str(delta) + "\n")
        stdout.flush()

    # determine covert bit based on timing
    if(abs(delta - ZERO) < abs(delta - ONE)):       # check if delta is closer to ZERO than ONE
        if(abs(delta - ZERO) < abs(delta - IGNORE)):
            covertBin += "0"
    else:
        if(abs(delta - ONE) < abs(delta - IGNORE)):
            covertBin += "1"

# convert the binary covert message into english
i = 0
while(i < len(covertBin)):
    b = covertBin[i:i + 8]
    n = int("0b{}".format(b),2)
    try:
        covert += unhexlify("{0:x}".format(n))
    except TypeError:
        covert += "?"
    i+=8


# close the connection to the server
s.close()

# display messaage
try:
    print "\nCovert Message: ",covert[:covert.rindex("EOF")]
except ValueError:
    print covert
