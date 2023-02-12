class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        for i in stones:
            heapq.heappush(max_heap, (-i, i))
        
        print(max_heap)
        
        while len(max_heap) > 1:
            max_item = heapq.heappop(max_heap)[1]
            next_item = heapq.heappop(max_heap)[1]
            new_item = max_item - next_item 
            heapq.heappush(max_heap, (-new_item, new_item))
            
        return heapq.heappop(max_heap)[1]
    
    
    

