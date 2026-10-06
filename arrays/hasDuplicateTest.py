import hasDuplicate
import unittest

class noDuplicates(unittest.TestCase):
    def testDups(self):
        nums = [1,2,3,3]
        self.assertTrue(hasDuplicate.setSolution.hasDuplicate(self, nums))
        self.assertTrue(hasDuplicate.lengthSolution.hasDuplicate(self, nums))

    def testNoDup(self):
        nums = [1, 2, 3]
        self.assertFalse(hasDuplicate.setSolution.hasDuplicate(self, nums))
        self.assertFalse(hasDuplicate.lengthSolution.hasDuplicate(self, nums))


def main():
    unittest.main()

if __name__ == "__main__":
    main()