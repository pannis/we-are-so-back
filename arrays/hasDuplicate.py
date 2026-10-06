from typing import List

# both solutions provided prevent the need for looping
# throughout the list multiple times


# works by saving it to the set then because a lookup
# in a set is O(1) we only have to iterate through
# once making it O(N)

class setSolution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


# works because sets cannot contain duplicates so if
# the length of the set is less than the length of the 
# list then that means there was a duplicate
class lengthSolution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)