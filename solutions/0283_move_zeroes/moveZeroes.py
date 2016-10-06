def moveZeroes(nums):
    lIdx = 0
    rIdx = 0

    while rIdx < len(nums) and lIdx < len(nums):
        lValue = nums[lIdx]
        rValue = nums[rIdx]

        if lValue == 0:
            while rValue == 0 and rIdx < len(nums) - 1 and lIdx < len(nums):
                rIdx += 1
                rValue = nums[rIdx]
            # found next non-zero num at this point
            nums[lIdx] = rValue
            nums[rIdx] = 0
            lIdx += 1
        else:
            lIdx += 1
            rIdx += 1