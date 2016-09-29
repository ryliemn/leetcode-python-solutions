# def addDigits(num):
#     while num > 9:
#         num = sum([int(c) for c in str(num)])
#     return num

def addDigits(num):
    return num % 9 if num % 9 > 0 or num == 0 else 9