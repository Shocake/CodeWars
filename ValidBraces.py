#Write a function that takes a string of braces, and determines if the order of the braces is valid. It should return true if the string is valid, and false if it's invalid.

def validBraces(string):
    braces = []
    open = ["{","[","("]
    close = ["}","]",")"]
    for i in string:
        if i in open:
            braces.append(i)
        elif i in close:
            pos = close.index(i)
            if ((len(braces) > 0) and (open[pos] == braces[len(braces)-1])):
                braces.pop()
    if len(braces) == 0:
        return True
    else:
        return False