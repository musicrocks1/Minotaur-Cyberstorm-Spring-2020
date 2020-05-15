###############################
# Program 3
# Jonah Landry
# 4/3/2020
# FTP Program PYTHON 3
################################

#Imports
from ftplib import FTP


#Variables isolated for easier testing
IP = "jeangourd.com"
port = 21
dir = "10/"
method = 10


def decode(binary,n): # binary = binary to be decoded n = the bit type (8 or 7)
    text = ""
    i = 0
    while (i < len(binary)):
        byte = binary[i:i+n]
        byte = int(byte,2)
        if (chr(byte) == "\b"):
            text = text[:-1]
        else:
            text += chr(byte)
        i += n

    return text

#Contents contains the original file list fetched from the ftp server. Text is for the final print. Binary is a temporary variable that stores each line of binary.
contents = []
text = ""
binary = ""

#Connects to the FTP server, logs in, navigates to the correct directory, saves the list of files to contents, and exits the server.
ftp = FTP(IP)
ftp.login()
ftp.cwd(dir)
ftp.dir(contents.append)
ftp.quit()

#Changes the original message into binary
for row in contents:
    #Resets the counter for which column we're currently reading.
    columnCount = 1
    for column in row:
        #If it's greater than 10 we want out since that's past the file directories.
        if columnCount > 10:
            break
        #When we're in the 7 method we want to ignore the entire line if anything in those first three isn't '-'
        elif columnCount <= 3 and method == 7:
            if (column != '-'):
                break
        #Otherwise commit a - as a 0 and anything else as a 1
        else:
            if (column == "-"):
                binary = binary + "0"
            else:
                binary = binary + "1"

        #Iterate counter
        columnCount = columnCount + 1

    #Add line to text and reset the temporary variable
    text = text + binary
    binary = ''



#If the method is equal to 7, it only runs the 7 bit decoder as it knows its going to be 7 bit.
if (method == 7):
    text = decode(text,7)
    print ("7-bit: ")
    print (text)
#Otherwise, it runs both decoders since 10 can be in 7 bit or 8 bit
elif (method == 10):
    text8 = decode(text,8)
    print ("8-bit: ")
    print (text8)
    text = decode(text,7)
    print ("7-bit: ")
    print (text)
#Just a little message here for error handling
else:
    print ("Invalid value for method. Try 10 or 7.")