##########################################
# Jonah Landry
# 4/24/2020
# Let's Chat (Client)
##########################################

# This program took me way longer than it should have and it was entirely because I was running on python3 instead of 2


#Imports
import socket
from sys import stdout
from time import time
from binascii import *

# enables debugging output
DEBUG = False

# set the server's IP address and port
ip = "138.47.102.67"
port = 33333

# create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server
s.connect((ip, port))

# Declare original covert_bin string
covert_bin = ""

#Declare ZERO and ONE
ZERO = 0.12
ONE = 0.18

# receive data until EOF
data = s.recv(4096) #char
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
    if (DEBUG):
        stdout.write(" {}\n".format(delta))
        stdout.flush()

    #Convert the data
    if (delta >= ONE):
        covert_bin += "1"
    else:
        covert_bin += "0"

# close the connection to the server
s.close()

#Decode the covert message
covert = ""
i = 0
temp = ""
EOF = ""
while (i< len(covert_bin)):
    #process one byte at a time
    b = covert_bin[i:i+8]

    #convert it to ASCII
    n = int("0b{}".format(b), 2)
    try:
        temp = unhexlify("{0:x}".format(n))
    except TypeError:
        temp = "?"

    #Looks for EOF as it's parsed before commited the character to the covert
    if(temp != "E" and EOF == ""):
        covert += temp
    elif(EOF == "" and temp== "E"):
        EOF += temp
    elif(EOF == "E" and temp=="O"):
        EOF += temp
    elif(EOF == "EO" and temp =="F"):
        break
    else:
        covert += EOF
        EOF = ""
    i += 8


print ("The covert message is: {}".format(covert))

