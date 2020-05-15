####################################################################################################################################################
# Name : Cullen Adams
# Date: 3/29/2020
# Assignment: Program 2: Vigenere Cypher
# Python Version: 2
# The following two sites were used for reference on how the Vigenere cypher works, and on how to remove spaces from a string:
# https://inventwithpython.com/hacking/chapter19.html
# http://www.datasciencemadesimple.com/remove-spaces-in-python/
####################################################################################################################################################
from sys import stdin, argv # Imports standard input (stdin) and a list of command line parameters (user arguments, called argv) from system (sys)

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # A simple way to store the table of symbols to be used in the cypher

def quit(): # A function to use when the program detects incorrect input
    print "Incorrect usage! Here's are some examples: python Vigenere.py -e \"This is my key\" OR python Vigenere.py -d mykey < text"
    exit(0)
    
def dencrypt(text, key, mode): # One function that both encrypts AND decrypts text
    output = "" # The string that we will store the encrypted/decrypted text in
    index = 0 # Keeps track of which letter of the key you are using
    key = key.upper() # Converts the key to all uppercase, in order to make sure the key works the same independent of its' case
    key = key.replace(" ", "") # Allows for the user to input a sentence instead of one string, by removing spaces from the key
    
    for letter in text: # Loops through each character in the given text
        num = ALPHABET.find(letter.upper()) # Ensures that the character is in our table of symbols, and gives it's value
        if num != -1: # If the last line returns -1, it means that the character was not in the "ALPHABET"
            if mode == "-e": # Adds the values of the letter in the key and the letter in text if encrypting
                num += ALPHABET.find(key[index])
            elif mode == "-d": # Subtracts the values of the letter in the key and the letter in text if decrypting
                num -= ALPHABET.find(key[index])
        
            num %= len(ALPHABET) # Avoids wrap-around error in the table
            
            # The following lines ensure that the letter case is maintained in the output
            if letter.isupper():
                output += ALPHABET[num]
            elif letter.islower():
                output += ALPHABET[num].lower()
        
            index +=1 # Moves to the next letter in the key
            if index == len(key): # Loops the key if the text is longer than the key
                index = 0
        else: # The symbol isn't in the "ALPHABET", so it isn't encrypted/decrypted, just kept the same
            output += letter
    
    return output

if (len(argv) < 3):
    quit()
mode = argv[1]
key = argv[2]

text = stdin.read().rstrip("\n") # As seen in the last 

if (mode == "-e"): # If the mode is encrypt, then pass that mode on to the function and print the outputted ciphertext
    ciphertext = dencrypt(text, key, mode)
    print ciphertext
elif (mode == "-d"): 
    plaintext = dencrypt(text, key, mode) #If the mode is decrypt, then pass that mode on to the function and print the outputted plaintext
    print plaintext
else: # If the argument given is not supported, show use case and quit
    quit()