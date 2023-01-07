class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = 0 
        for i in range(i,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j] 
        return []



#1 nums에서 숫자 하나를 고른다
#2 target에서 #1을 뺀 값이 있는지 확인한다. 없으면 다시 한다. 
# big o = n^2 

