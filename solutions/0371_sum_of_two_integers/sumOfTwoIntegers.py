def getSum(a, b):
    return  a if b == 0 else getSum(a ^ b, (a & b) << 1)