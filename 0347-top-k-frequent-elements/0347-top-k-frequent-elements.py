class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #1 dict = {'number' : 'appearance'} - one pass O(n)
        d = collections.defaultdict(int)
        for num in nums :
            d[num] += 1 
            
        #2 sort dict key by dict value -> O(n)
        newdict = dict(sorted(d.items(),reverse=True, key=lambda item: item[1]))
        #3 dict.keys()[:k]
        
        return list(newdict.keys())[:k]
        