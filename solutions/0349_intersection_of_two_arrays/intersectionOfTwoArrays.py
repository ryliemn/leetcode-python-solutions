def intersection(nums1, nums2):
    nums1Set = set(nums1)
    nums2Set = set(nums2)
    intersection = nums1Set & nums2Set

    return list(intersection)