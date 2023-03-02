import math

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0 
        r = len(height)-1
        
        maxArea = min(height[l], height[r]) * abs(r-l)
        
        #left, right중 큰 애를 두고, 작은 애를 움직인다. 
        #하나가 바뀌면, 다시 maxArea 계산
        #예외: 3......13..3 의 경우 생각해야함 
        while True:
            if r <= l:
                break

            if height[l] < height[r]:
                l += 1 
            else: 
                r -= 1
            
            maxArea = max(maxArea, min(height[l], height[r]) * abs(r-l))
            
        
        return maxArea 