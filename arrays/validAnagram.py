# checks if two strings are valid anagrams
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if lengths aren't equal then don't have
        # to check the rest 
        if len(s) != len(t): return False

        # function for making a dictionary for a 
        # string where each letter is the key and
        # number of times the letter shows up is 
        # the value
        def makeDict(word: str) -> dict:
            xDict = {}
            for letter in word:
                if letter in xDict:
                    xDict[letter] += 1
                else:
                    xDict[letter] = 1
            return xDict
        
        # compares the two strings dictionaries
        # to see if they are the same and returns
        # the result as our answer
        return makeDict(s) == makeDict(t)