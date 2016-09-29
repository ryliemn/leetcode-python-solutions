def singleNumber(nums):
    from functools import reduce
    from operator import xor
    return reduce(xor, nums)