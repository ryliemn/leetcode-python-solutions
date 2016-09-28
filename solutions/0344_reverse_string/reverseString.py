def reverseString(s):
    return s[::-1]

def reverseStringRecursive(s):
    if len(s) == 0:
        return s
    else:
        return s[-1] + reverseStringRecursive(s[0:-1])