from sys import stdin

message = stdin.read().rstrip("\n")

message = message.replace("X", " ")

print(message)
