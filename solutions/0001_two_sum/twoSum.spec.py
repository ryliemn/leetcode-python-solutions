import unittest
from twoSum import twoSum

class TestTwoSum(unittest.TestCase):
    def testGivenExample(self):
        nums = [2, 7, 11, 15]
        target = 9

        returned = twoSum(nums, target)
        expected = [0, 1]

        self.assertEqual(returned, expected)

    def testUnsortedNums(self):
        nums = [8, 7, 3, 15, 5]
        target = 18

        returned = twoSum(nums, target)
        expected = [2, 3]

        self.assertEqual(returned, expected)

    def testRepeatedNums(self):
        nums = [5, 8, 1, 5, 3, 23]
        target = 10

        returned = twoSum(nums, target)
        expected = [0, 3]

        self.assertEqual(returned, expected)

if __name__ == '__main__':
    unittest.main()