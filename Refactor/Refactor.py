#!usr/bin/python3

import sys
#
#
#

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
#
#
#

length = len(lines)

print("There are", length, "lines.")

print(*lines, sep='\n')

# Setup 2 dimensional array
matches = [[] for i in range(length)]
#
#
#

# Build array.
for i in range(length):
    index = -1
    for j in range(length):
        index += 1
        if lines[i] == lines[j] :
            # if lines i and j match append i at index.
            matches[index].append(i)


# Check the array.
# for each i, search for consecutive numbers to find chunks of code
# that have been copied.
for i in range(length):
    print('i: ', i)
    print(*matches[i], sep=' ')


