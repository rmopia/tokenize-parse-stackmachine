from tokenize_parse import Tokenize
from tokenize_parse import Parse
from stack_machine import StackMachine
import sys

file = open(sys.argv[1], "r")
data = file.readlines()

i = 0
for line in data:
    data[i] = line.strip() # process removes '\n' from file contents
    i += 1

lineList = [] # lineList will be a list of lists

for line in data:
    try:
        tokens = Tokenize(line) # tokenizes lines that are then added to another list
        lineList.append(tokens)
    except ValueError:
        print("Unexpected token: " + str(line))
        exit()

for items in lineList:
    try:
        if Parse(items) is True: # ensures all tokenized items are valid via the parse function
            continue
    except ValueError:
        print("Unexpected line: " + str(items))
        exit()

s = StackMachine()

while s.currentLine < len(lineList):
    if s.currentLine < 0:
        print("Trying to execute invalid line: " + str(s.currentLine)) # statement to catch any negative indices
    else:
        try:
            res = s.execute(lineList[s.currentLine])
            if res is not None: # only prints out popped values unless they're errors
                print(res)
        except IndexError:
            print("Line " + str(s.currentLine) + ": '" + str(lineList[s.currentLine][0]) + "' caused Invalid Memory Access")

    s.currentLine += 1

print("Program terminated correctly")



