import unittest
from findTheDifference import findTheDifference

class TestFindTheDifference(unittest.TestCase):
    def testGivenExample(self):
        s = "abcd"
        t = "abcde"

        returned = findTheDifference(s, t)
        expected = 'e'

        self.assertEqual(returned, expected)

if __name__ == '__main__':
    unittest.main()