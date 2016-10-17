import unittest
from fizzBuzz import fizzBuzz

class TestFizzBuzz(unittest.TestCase):
    def testGivenExample(self):
        n = 15

        returned = fizzBuzz(n)
        expected = ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']

        self.assertEqual(returned, expected)


if __name__ == '__main__':
    unittest.main()