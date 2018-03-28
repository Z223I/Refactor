#!usr/bin/python3

import sys

# Ask for file if not on the command line
if len(sys.argv) < 2:
    filename = input("Filename: ")
else:
    filename = sys.argv[1]
    print(filename)

# Open file
with open(filename, "r") as fo:
    lines = fo.readlines()

lines = [x.strip() for x in lines]

length = len(lines)

print("There are", length, "lines.")

print(*lines, sep='\n')

# Setup 2 dimensional array
matches = [[] for i in range(length)]

for i in range(length):
    matches[i].append(1)