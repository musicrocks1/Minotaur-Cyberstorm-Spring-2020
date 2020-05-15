#Name: Joseph Siharath
#Due Date: March 3, 2020
#Description: This program connects to a FTP server and decodes a binary message
# hidden in the permissions of the file and prints the message.

#NOTE: This program was coded using Python 3.8.2

from ftplib import FTP

#Constants and FTP server info
METHOD = 10

IP = "jeangourd.com"
PORT = 8008
FOLDER = "/.secretstorage/.folder2/.howaboutonemore"

# Arrays to download the information from the ftp server and store it for the program
# to use
contents = []
perms = ""
binary = ""

# Connecting to the FTP server and downloading the contents of a specified directory
ftp = FTP()
ftp.connect(IP, PORT)
ftp.login(user='valkyrie', passwd='chooseroftheslain')
ftp.cwd(FOLDER)
ftp.dir(contents.append)
ftp.quit()

# Function to decode binary message
def decode(binary, n):
	text = ""
	i = 0
	while (i < len(binary)):
		byte = binary[i:i+n]
		byte = int(byte, 2)
		if (byte == 10):
			text = text[:-1]
		else:
			text += chr(byte)
		i += n

	return text

# If the method specified is 7, skip the first 3 bits and read the next 7 bits
# convert the perms to binary "-" = 0 and anything else is 1
if (METHOD == 7):
        for row in contents:
                print (row)
                if (row[0:3] == "---"):
                
                        perms += row[3:10]
        for x in range(len(perms)):
                if (perms[x] == "-"):
                        binary += "0"
                else:
                        binary += "1"
        text = decode(binary, 7)

# If method specified is 10, read and convert the first 10 bits where "-" = 0 and
# anythig else is 1
if (METHOD == 10):
        for row in contents:
                perms += row[0:10]
        for x in range(len(perms)):
                if (perms[x] == "-"):
                        binary += "0"
                else:
                        binary += "1"
        text = decode(binary, 7)

# Print out the message
print (text)
