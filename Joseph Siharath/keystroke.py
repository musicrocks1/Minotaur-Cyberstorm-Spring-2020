from pynput.keyboard import Key, Controller
from time import sleep
from random import uniform
from termios import tcflush, TCIFLUSH
from sys import stdin, stdout


password = raw_input()
timings = raw_input()
keyboard = Controller()

string ="My password is incorrect."

print "Password = {}".format(password)
print "timings = {}".format(timings)

#password = password.split(",")
password = password[:len(password) / 2+1]
password = "".join(password)

print password

#timings = timings.split(",")
timings = [float(a) for a in timings]
keypress = timings[:len(timings) / 2+1]
keyintervals = timings[len(timings) / 2+1:]

sleep(6)

for char in string:
	keyboard.press(char)
	sleep(uniform(0.02, 0.3))
	keyboard.release(char)

print "Keypress times = {}".format(keypress)
print "Keyinterval times = {}".format(keyintervals)

#tcflush(stdin, TCIFLUSH)

print


