def twoSum(nums, target):
    def getIndices(nums, x, y):
        numsCopy = nums[:]
        indices = []

        xIndex = numsCopy.index(x)
        indices.append(xIndex)
        numsCopy[xIndex] = None

        yIndex = numsCopy.index(y)
        indices.append(yIndex)

        return indices

    sortedNums = sorted(nums)
    left = 0
    right = len(sortedNums) - 1

    while left < right:
        currentSum = sortedNums[left] + sortedNums[right]
        if currentSum == target:
            return getIndices(nums, sortedNums[left], sortedNums[right])
        elif currentSum < target:
            left += 1
        elif currentSum > target:
            right -= 1

    return positions