from collections import defaultdict

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = defaultdict(int)
        while len(nums) > 0 :
            n = nums.pop()
            if n in d.keys():
                return True
            else:
                d[n] = 1 
        return False 

