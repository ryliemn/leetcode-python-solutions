import unittest
from sumOfTwoIntegers import getSum

class TestSumOfTwoIntegers(unittest.TestCase):
    def testGivenExample(self):
        a = 1
        b = 2

        returned = getSum(a, b)
        expected = 3

        self.assertEqual(returned, expected)

if __name__ == '__main__':
    unittest.main()