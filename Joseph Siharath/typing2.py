from pynput.keyboard import Key, Controller
from time import sleep
from random import uniform
from termios import tcflush, TCIFLUSH
from sys import stdin, stdout

sleep(6)

keyboard = Controller()

password = ['D', 'r', '.', ' ', 'K', 'i', 'r', 'e', 'm', 'i', 'r', 'e', ' ', 'k', 'n', 'o', 'w', 's', ' ', 'h', 'i', 's', ' ', 's', 't', 'u', 'f', 'f', '.', 'Dr', 'r.', '. ', ' K', 'Ki', 'ir', 're', 'em', 'mi', 'ir', 're', 'e ', ' k', 'kn', 'no', 'ow', 'ws', 's ', ' h', 'hi', 'is', 's ', ' s', 'st', 'tu', 'uf', 'ff', 'f.']





timings =  ['0.94', '0.63', '0.39', '0.38', '0.12', '0.30', '0.83', '0.58', '0.67', '0.30', '0.22', '0.83', '0.73', '0.11', '0.41', '0.59', '0.75', '0.63', '0.24', '0.89', '0.78', '0.24', '0.39', '0.43', '0.38', '0.82', '0.31', '0.36', '0.14', '0.54', '0.68', '0.74', '0.17', '0.24', '0.48', '0.87', '0.91', '0.78', '0.36', '0.44', '0.45', '0.90', '0.64', '0.23', '0.68', '0.38', '0.30', '0.64', '0.44', '0.37', '0.68', '0.78', '0.97', '0.22', '0.56', '0.69', '0.55']





#stdin.flush()

#password = password.split(",")
password = password[:(len(password)/2) + 1]
#password = "".join(password)

#timings = timings.split(",")
timings = [float(a) for a in timings]
keyPresses = timings[:(len(timings)/2) + 1]
keyIntervals = timings[(len(timings)/2) + 1:]
keyIntervals.append(0.0);

for i in range(len(password)):
    keyboard.press(password[i])
    sleep(keyPresses[i])
    keyboard.release(password[i])
    sleep(keyIntervals[i])
keyboard.press(Key.enter)
keyboard.release(Key.enter)

tcflush(stdin, TCIFLUSH)
