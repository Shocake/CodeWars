#Implement the function unique_in_order which takes as argument a sequence and returns a list of items without 
#any elements with the same value next to each other and preserving the original order of elements.

def unique_in_order(iterable):
    input = iterable
    reallist = []
    for i in input:
        if not reallist:
            reallist.append(i)
        elif reallist[-1]!=i:
            reallist.append(i)

    return reallist