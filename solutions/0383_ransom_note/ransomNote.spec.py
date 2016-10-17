import unittest
from ransomNote import canConstruct

class TestRansomNote(unittest.TestCase):
    def testGivenExampleOne(self):
        ransomNote = "a"
        magazine = "b"

        returned = canConstruct(ransomNote, magazine)
        expected = False

        self.assertEqual(returned, expected)

    def testGivenExampleTwo(self):
        ransomNote = "aa"
        magazine = "ab"

        returned = canConstruct(ransomNote, magazine)
        expected = False

        self.assertEqual(returned, expected)
      
    def testGivenExampleThree(self):
        ransomNote = "aa"
        magazine = "aab"

        returned = canConstruct(ransomNote, magazine)
        expected = True

        self.assertEqual(returned, expected)

if __name__ == '__main__':
    unittest.main()