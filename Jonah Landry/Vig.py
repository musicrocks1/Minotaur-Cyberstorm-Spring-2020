################################3
# Python 3
# Jonah Landry
# Vig Cypher
# Due March 30th
##################################

#Import from sys to get command line input
from sys import stdin, argv

# A quick preface on Ord
# While I started this code I figured there was some simpler way to convert between numbers and letters and be able to add them and the like
# and I found out about ord in the process. While it was very useful at first, it proved to be too tricky to use with the encoding and decoding itself
# as such I've taken it out of the algorithms, though it does still show up from time to time in the code. The function ord(x) returns a sort of pseudo unicode
# of the character x which then translates back to a character with char.

#Takes out anything that's not alphabetic from the key (since the ord value for a is 97 and z is 122, anything outside this range is discarded)
def keyClean (key):
    key = key.lower()
    newKey = []
    i = 0
    while (i < len(key)):
        if (alphToNum(key[i]) != -1):
            newKey.append(key[i])
        i = i + 1
    return ("".join(newKey))

def alphToNum (query):
    i = 0
    query = query.lower()
    found = False
    # variable to represent the alphabet
    alph = "abcdefghijklmnopqrstuvwxyz"
    while (i < len(alph)):
        if (alph[i] == query):
            iFinal = i
            found = True
        i = i + 1
    if (found):
        return iFinal
    else:
        return -1

def numToAlph(query):
    alph= "abcdefghijklmnopqrstuvwxyz"
    return alph[query]
#decrypts
def decrypt(cyphertext, key):
    # Blank array for plaintext, creating iterators for text and key, and a reference for the alphabet
    textCount = 0
    keyCount = 0
    plaintext = []

    # While loop that iterates each character
    while (textCount < len(cyphertext)):

        # This if checks if the current character is in the alphabet
        if (alphToNum(cyphertext[textCount]) != -1):

            # Uses the alphToNum function to get a number for key and text and adds them, taking remander after division by 26 to get a letter
            tempNum = (alphToNum(cyphertext[textCount]) - alphToNum(key[keyCount])) % 26

            # Changes the number back to a letter by using corresponding letter from the string alph
            tempChr = numToAlph(tempNum)
            print(tempChr)

            # If the cyphertext matches itself in lower case, then its fine to keep the cypher as is since its lowercase only. If not, it capitalizes it
            if (cyphertext[textCount].lower() == cyphertext[textCount]):
                plaintext.append(tempChr)
            else:
                plaintext.append(tempChr.upper())

            # Iterates the key, resetting if it gets to the end of the key.
            keyCount = keyCount + 1
            if (keyCount >= len(key)):
                keyCount = 0

        # If the character isn't alphabetical, it isn't encrypted
        else:
            plaintext.append(cyphertext[textCount])
        # Iterates the text counter as it finished with each letter
        textCount = textCount + 1



    return ("".join(plaintext))

#Encrypts
def encrypt(plaintext, key):
    #Blank array for cipher text, creating iterators for text and key, and a reference for the alphabet
    ciphertext = []
    textCount = 0
    keyCount = 0
    alph = "abcdefghijklmnopqrstuvwxyz"

    #While loop that iterates each character
    while (textCount < len(plaintext)):

        #This if checks if the current character is in the alphabet
        if (alphToNum(plaintext[textCount]) != -1):

            #Uses the alphToNum function to get a number for key and text and adds them, taking remander after division by 26 to get a letter
            tempNum = (alphToNum(plaintext[textCount]) + alphToNum(key[keyCount]))%26

            #Changes the number back to a letter by using corresponding letter from the string alph
            tempChr = alph[tempNum]


            #If the plaintext matches itself in lower case, then its fine to keep the cypher as is since its lowercase only. If not, it capitalizes it
            if (plaintext[textCount].lower() == plaintext[textCount]):
                ciphertext.append(tempChr)
            else:
                ciphertext.append(tempChr.upper())

            # Iterates the key, resetting if it gets to the end of the key.
            keyCount = keyCount + 1
            if (keyCount >= len(key)):
                keyCount = 0

        #If the character isn't alphabetical, it isn't encrypted
        else:
            ciphertext.append(plaintext[textCount])
        # Iterates the text counter as it finished with each letter
        textCount = textCount + 1



    return ("".join(ciphertext))

#Expecting command line of "python Vig.py [mode] [key]" and then input
mode = argv[1]
key = argv[2]

#Cleans up the key for use
key = keyClean(key)
print(key)

#Cleans up the text for use

#Gets first line of input
text = stdin.readline()
while(text != ""): #If in linux terminal, will exit with ^D otherwise use ^C
    if (mode == "-e"): #encrypt if mode is -e
        ciphertext = encrypt(text, key)
        print (ciphertext)
    elif(mode == "-d"): #decrypt line if -d mode
        plaintext = decrypt(text,key)
        print (plaintext)
    else: #error if wrong mode
        print("Error! Invalid mode '", mode, "'. Expected '-e' or '-d'")

    text = stdin.readline()
