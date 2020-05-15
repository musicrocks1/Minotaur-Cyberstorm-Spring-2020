# python 2
from ftplib import FTP

# FTP method
METHOD = 7

# global variables for FTP
IP = "138.47.99.163"
PORT = 21
FOLDER = "FILES"

# returns string of 
# binary = string of numbers to be turned into text
# n = number of bits per byte
def decode(binary, n):
    text = ""
    i = 0
    # get string of length n to turn into byte
    # convert byte to integer, use this integer as ASCII code to get character
    # append character to text
    while (i < len(binary)):
        byte = binary[i:i + n]
        byte = int(byte, 2)
        # remove previous character if byte == backspace ASCII code (8)
        if (byte == 8):
            text = text[:-1]
        else:
            text += chr(byte)
        i += n
    # return message
    return text

# to hold file list
contents = []

# connect to FTP server at IP and PORT, login, navigate to FOLDER, get file list, and disconnect
ftp = FTP()
ftp.connect(IP, PORT)
ftp.login("valkyrie", "readytodie")
ftp.cwd(FOLDER)
ftp.dir(contents.append)
ftp.quit()

# to hold string of bits to convert into message
bitString = ""

# if METHOD is 7, ignore rows with junk in the first 3 indices
# for both METHOD values (7 or 10), go through each line and append 0 to bitString
#     if the char in its bit range == "-", otherwise append 1
for row in contents:
    if METHOD == 7 and row[0:3] == "---":
        for i in range(3, 10):
            if row[i] == "-":
                bitString += "0"
            else:
                bitString += "1"
    elif METHOD == 10:
        for i in range(10):
            if row[i] == "-":
                bitString += "0"
            else:
                bitString += "1"

# decode message as 7-bit if METHOD == 7
# decode message as both 7-bit and 8-bit if METHOD == 10
if METHOD == 7:
    print decode(bitString, 7)
elif METHOD == 10:
    print decode(bitString, 7)
    print decode(bitString, 8)
