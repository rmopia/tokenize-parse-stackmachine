class StackMachine:
    def __init__(self):
        self.stack = []
        self.currentLine = 0 # numerical iterator used during driver program
        self.lst = [None] * 15 # empty list that will be used during the save and get functions

    def push(self, value):
        self.stack.append(int(value)) # string 'value' is casted as an integer into the stack to support stack operations
        return None

    def pop(self):
        if len(self.stack) == 0: # if the stack is empty
            raise IndexError("Invalid Memory Access")
        else:
            return self.stack.pop()

    def add(self):
        v1 = self.pop()
        v2 = self.pop()
        self.push(int(v1) + int(v2))
        return None

    def sub(self):
        v1 = self.pop()
        v2 = self.pop()
        self.push(int(v1) - int(v2))
        return None

    def mul(self):
        v1 = self.pop()
        v2 = self.pop()
        product = int(v1) * int(v2)
        self.push(product)
        return None

    def div(self):
        v1 = self.pop()
        v2 = self.pop()
        quotient = int(v1) / int(v2)
        self.push(quotient)
        return None

    def mod(self):
        v1 = self.pop()
        v2 = self.pop()
        self.push(int(v1) % int(v2))
        return None

    def skip(self): # increments currentLine iterator if the first popped value is zero (note: currentLine will still increment + 1 outside)
        v1 = self.pop()
        v2 = self.pop()
        if v1 == 0:
            self.currentLine += v2
            return None
        return None

    def save(self, index): # saves popped value and is put into the specified index
        self.lst[int(index)] = self.pop()
        return None

    def get(self, index): # gets a saved popped value from the specified index
        got = self.lst[int(index)]
        if got is None: # if the index specified doesn't return a value
            raise IndexError("Invalid Memory Access")
        else:
            self.push(got)
            return None

    def execute(self, tokens): # takes a tokenized & parsed list from a list of lists from the driver program and starts required behavior 
        if tokens[0] == "push":
            return self.push(tokens[1])
        elif tokens[0] == "pop":
            return self.pop()
        elif tokens[0] == "add":
            return self.add()
        elif tokens[0] == "sub":
            return self.sub()
        elif tokens[0] == "mul":
            return self.mul()
        elif tokens[0] == "div":
            return self.div()
        elif tokens[0] == "mod":
            return self.mod()
        elif tokens[0] == "skip":
            return self.skip()
        elif tokens[0] == "save":
            return self.save(tokens[1])
        else:
            return self.get(tokens[1])
            
            
