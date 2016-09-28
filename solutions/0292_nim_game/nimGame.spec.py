import unittest
from nimGame import canWinNim

class TestNimGame(unittest.TestCase):
    def testGivenExample(self):
        n = 4

        returned = canWinNim(n)
        expected = False

        self.assertEqual(returned, expected)

    def testFiveN(self):
        n = 5

        returned = canWinNim(n)
        expected = True

        self.assertEqual(returned, expected)

    def testMemory(self):
        n = 1348820612

        returned = canWinNim(n)
        expected = False

        self.assertEqual(returned, expected)

if __name__ == '__main__':
    unittest.main()