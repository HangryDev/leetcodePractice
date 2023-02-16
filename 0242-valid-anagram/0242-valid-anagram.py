from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = defaultdict(int)
        d1 = defaultdict(int)
        for words in s:
            d[words] += 1
        
        for words in t:
            d1[words] +=1 
            
        if d == d1: 
            return True

        return False
            
            
        
        