#Given an array of integers, find the one that appears an odd number of times.

#There will always be only one integer that appears an odd number of times.

def find_it(seq):
    for i in seq:
        x=seq.count(i)
        if x%2==1:
            return i