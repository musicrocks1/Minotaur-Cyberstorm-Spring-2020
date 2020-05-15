
#Used for taking commands from command line
import sys

def cleanse(input):
    output = ""
    for charIn in input:
        if (charIn == "0" or charIn == "1"):
            output = output + charIn
    return output


#Expected "binCleanse.py filename
arguments = sys.argv[1:]
givenFile = open(arguments[0])
givenText = givenFile.read()
cleansedBin = cleanse(givenText)
print(cleansedBin)
