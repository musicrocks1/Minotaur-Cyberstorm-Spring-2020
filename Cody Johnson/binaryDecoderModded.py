from sys import stdin

##binary = string of numbers to be turned into text
##n = number of bits per byte
def decode(binary, n):
    ##variable to store decoded string
    text = ""
    ##variable for indexing
    i = 0
    ##run while the end of the binary string has not been reached
    while (i < len(binary)):
        ##get 7/8 digit long string
        byte = binary[i:i + n]
        ##convert number in base 2 into base 10
        byte = int(byte, 2)
        ##if the character would represent a backspace
        if (byte == 8):
            ##truncate the end of the text
            text = text[:-1]
        else:
            ##append the character to the end of the text
            text += chr(byte)
        ##increase the index by 7/8
        i += n
    ##return decoded string
    return text

##read string of numbers
binary = stdin.read().rstrip("\n")

##if the text contains 7-bit ASCII
#if (len(binary) % 7 == 0):
text = decode(binary, 7)
print "7-bit: "
print text
print
##if the text contains 8-bit ASCII
#if (len(binary) % 8 == 0):
text = decode(binary, 8)
print "8-bit: "
print text
