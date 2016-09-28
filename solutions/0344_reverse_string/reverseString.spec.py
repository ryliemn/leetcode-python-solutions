import unittest
from reverseString import reverseString, reverseStringRecursive

class TestReverseString(unittest.TestCase):
    def testGivenExample(self):
        s = 'hello'

        returned = reverseString(s)
        returnedRecursive = reverseStringRecursive(s)
        expected = 'olleh'

        self.assertEqual(returned, expected)
        self.assertEqual(returnedRecursive, expected)

    def testEmptyString(self):
        s = ''

        returned = reverseString(s)
        returnedRecursive = reverseStringRecursive(s)
        expected = ''

        self.assertEqual(returned, expected)
        self.assertEqual(returnedRecursive, expected)

    def testEvenLengthString(self):
        s = 'hellos'

        returned = reverseString(s)
        returnedRecursive = reverseStringRecursive(s)
        expected = 'solleh'

        self.assertEqual(returned, expected)
        self.assertEqual(returnedRecursive, expected)

if __name__ == '__main__':
    unittest.main()