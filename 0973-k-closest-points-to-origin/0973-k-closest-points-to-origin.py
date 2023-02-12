class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #1 points에 대해서 유클리디안 거리 측정 
        # distSqrd = point[0]**2 + point[1]**2

        return sorted(points, key = lambda x: x[0]**2 + x[1]**2 )[:k]
        
            
        
        