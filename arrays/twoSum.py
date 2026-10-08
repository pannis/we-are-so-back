class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        numDict = {}
        # learned you could instead use enumerate(nums)
        # which would give you i, n with i being the index
        # and n being the number at that index
        for i in range(len(nums)):
            secondAns = target - nums[i]
            if secondAns in numDict:
                return [numDict[secondAns], i]
            numDict[nums[i]] = i