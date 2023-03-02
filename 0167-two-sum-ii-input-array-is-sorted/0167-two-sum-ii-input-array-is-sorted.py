class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        setN = set(numbers)
        output = [0,0]
        for i in numbers:
            if (target - i) in setN: 
                output[0] = numbers.index(i) + 1 
                numbers.remove(i)
                output[1] = numbers.index(target-i) + 2
                break
        
        return output
        