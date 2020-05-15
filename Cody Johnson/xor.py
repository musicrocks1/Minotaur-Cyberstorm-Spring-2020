# python 3

from sys import stdin, stdout


# name of file containing key
keyFile = "key"


# try to read binary contents of keyFile into keyFileContents
try:
    with open(keyFile, "rb") as myfile:
        keyFileContents = myfile.read()
# otherwise, error
except FileNotFoundError:
    print("Error: Key file does not exist in current directory.")
    exit()


# try to read given binary file into byteStr
try:
    byteStr = stdin.buffer.read()
# otherwise, error
except AttributeError:
    print("Error: No input file provided.")
    exit()


# perform xor operation between each byte of the bytes variables, and
#     append each result to the xor array
# if the key is not the same length as the given file, loop the key
#     from the beginning again
xor = []
for i in range(len(byteStr)):
    xor.append(byteStr[i] ^ keyFileContents[i % len(keyFileContents)])


# convert xor array to bytearray and output result
stdout.buffer.write(bytearray(xor))
