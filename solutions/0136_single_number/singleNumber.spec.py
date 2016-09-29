import unittest
from singleNumber import singleNumber

class TestSingleNumber(unittest.TestCase):
    def testOrdinaryExample(self):
        nums = [1, 5, 3, 1, 5]

        returned = singleNumber(nums)
        expected = 3

        self.assertEqual(returned, expected)

    def testLargeExample(self):
        nums = [1, 9, 5, 6, 3, 7, 2, 2, 7, 1, 5, 9, 3]

        returned = singleNumber(nums)
        expected = 6

        self.assertEqual(returned, expected)

if __name__ == '__main__':
    unittest.main()