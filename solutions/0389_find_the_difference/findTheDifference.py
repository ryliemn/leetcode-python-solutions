def findTheDifference(s, t):
    from functools import reduce
    ordVals = [ord(c) for c in s + t]
    return chr(reduce(lambda acc, val: acc ^ val, ordVals))