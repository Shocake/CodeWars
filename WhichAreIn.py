#Given two arrays of strings a1 and a2 return a sorted array r in lexicographical order of the strings of a1 which are substrings of strings of a2.

def in_array(array1, array2):
    r = []
    for i in array1:
        for i2 in array2:
            if i in i2 and i not in r:
                r.append(i)
    r.sort()
    return r