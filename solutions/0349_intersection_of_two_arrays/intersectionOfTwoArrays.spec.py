import unittest
from intersectionOfTwoArrays import intersection

class TestIntersection(unittest.TestCase):
    def testGivenExample(self):
        nums1 = [1, 2, 2, 1]
        nums2 = [2, 2]

        returned = intersection(nums1, nums2)
        expected = [2]

        self.assertEqual(returned, expected)

if __name__ == '__main__':
    unittest.main()