class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        len1 = len(s1)
        len2 = len(s2)

        counterS1 = Counter(s1)
        
        for i in range(len2-len1+1): 
            substr = s2[i: i+len1]
            if counterS1 == Counter(substr):
                return True
        
        return False 
        
        
