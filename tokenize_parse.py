def isInt(token): # checks whether a item is a number by casting it
    try:
        int(token)
        return True
    except:
        return False

def Tokenize(str):
    for token in str.split(): # split function creates a list of strings
        if token == "push" or token == "pop" or token == "add" or token == "sub" or token == "mul" or token == "div"\
                or token == "mod" or token == "skip" or token == "save" or token == "get":
            continue
        elif isInt(token):
            continue
        else:
            raise ValueError
    return str.split()

def Parse(tokens): # boolean function that checks whether a line is valid by being in the proper format
    i = 0
    if len(tokens) == 2:
        while i < len(tokens) - 1:
            if (tokens[i] == "push" or tokens[i] == "save" or tokens[i] == "get") and isInt(tokens[i + 1]):
                return True
            else:
                raise ValueError
        i += 1  
    elif len(tokens) == 1:
        while i < len(tokens):
            if tokens[i] == "pop" or tokens[i] == "add" or tokens[i] == "sub" or tokens[i] == "mul" or tokens[i] == "div"\
                    or tokens[i] == "mod" or tokens[i] == "skip":
                return True
            else:
                raise ValueError
    else:
        raise ValueError
        
        
