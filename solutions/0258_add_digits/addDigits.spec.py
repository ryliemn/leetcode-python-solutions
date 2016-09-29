import unittest
from addDigits import addDigits

class TestAddDigits(unittest.TestCase):
    def testGivenExample(self):
        num = 38

        returned = addDigits(num)
        expected = 2

        self.assertEqual(returned, expected)

    def testZero(self):
        num = 0

        returned = addDigits(num)
        expected = 0

        self.assertEqual(returned, expected)

if __name__ == '__main__':
    unittest.main()