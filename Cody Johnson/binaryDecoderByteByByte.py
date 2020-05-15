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

index = 0
mode = 7
text = ""

while index <= len(binary) - 1:
    if mode == 7:
        mode = 8
        text += decode(binary[index:index + 7], 7)
        index += 7
    else:
        mode = 7
        text += decode(binary[index:index + 8], 8)
        index += 8

print text
