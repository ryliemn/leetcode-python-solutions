import unittest
from moveZeroes import moveZeroes

class TestMoveZeroes(unittest.TestCase):
    def testGivenExample(self):
        nums = [0, 1, 0, 3, 12]

        moveZeroes(nums)
        expected = [1, 3, 12, 0, 0]

        self.assertEqual(nums, expected)

    def testLargerExample(self):
        nums = [1, 2, 0, 3, 0, 4, 5, 6, 0, 0, 7, 8, 0, 9, 0]

        moveZeroes(nums)
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0, 0, 0]

        self.assertEqual(nums, expected)

if __name__ == '__main__':
    unittest.main()