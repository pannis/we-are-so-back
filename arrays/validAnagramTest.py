import validAnagram
import unittest

class anagramsTests(unittest.TestCase):
    def testNotValid(self):
        solution = validAnagram.Solution()
        self.assertFalse(solution.isAnagram("jar", "jam"))

    def testIsValid(self):
        solution = validAnagram.Solution()
        self.assertTrue(solution.isAnagram("racecar", "carrace"))

def main():
    unittest.main()

if __name__ == "__main__":
    main()