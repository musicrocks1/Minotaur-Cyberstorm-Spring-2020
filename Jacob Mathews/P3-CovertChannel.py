############################################################################################
# Jacob Mathews
# Program 3: Covert Channel
# Python 2.7
# 4/3/20
############################################################################################
from ftplib import FTP

# mode globals
METHOD = 10                      # method for encoding, either 7 or 10
BIT = 7                         # grouping of bits used for decoding binary, either 7 or 8

# FTP globals
IP = "138.47.99.163"
PORT = 21
FOLDER = "FILES"
USERNAME = "valkyrie"
PASSWORD =  "readytoride"

# contents within specified folder
contents = []


# convert a string of zeros and ones using the ASCII table (n bits -> one ASCII value)
def binaryDecode(binary, n):
    text = ""
    i = 0
    while (i<len(binary)):
        byte = binary[i:i+n]    # look at sections of the binary based on parameter passed
        byte = int(byte,2)      # convert to base 10

        if(byte == 8):          # special case when backspace is decoded
            text = text[:-1]    # returns the string without the last character

        else:                   # all other characters
            text+=chr(byte)
        i+=n

    return text

# parses the array of strings from the ftp server and returns the translated message
def translateContents(contents):
    binaryMessage=""                            # holds message in binary

    # iterates through each file and translates to binary then calls binaryDecode to translate to plaintext
    if(METHOD == 7):
        for row in contents:
            if(row[:3] == "---"):               # if there as a set bit in the first three, ignore

                # translate next 7 characters to binary
                for f in row[3:10]:
                    if(f=="-"):
                        binaryMessage+="0"
                    else:
                        binaryMessage+="1"

        return binaryDecode(binaryMessage,7)

    # iterates through each file and translates to binary then calls binaryDecode to translate to plaintext
    elif(METHOD == 10):
        for row in contents:

            #translate first 10 characters to binary
            for f in row[:10]:
                if(f=="-"):
                    binaryMessage+="0"
                else:
                    binaryMessage+="1"

        return binaryDecode(binaryMessage,BIT)


    else:                                       # incase of typo
        return "Invalid METHOD value, must be 7 or 10"


## connect to FTP server using the specified IP & PORT, retrieve the contents of the
## specifed folder, then disconnect from the server
ftp = FTP()
ftp.connect(IP,PORT)
ftp.login(USERNAME,PASSWORD)
ftp.cwd(FOLDER)
ftp.dir(contents.append)
ftp.quit()

# translates folder contents to binary, then binary to plaintext
print translateContents(contents)
