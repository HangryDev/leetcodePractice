class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1 = len(s1)
        len2 = len(s2)
        asc1 = sum([ord(char) for char in s1])  
        candidates = [] 
                    
        counterS1 = Counter(s1)
        
        for i in range(len2-len1+1): 
            substr = s2[i: i+len1]
            substr_asc = sum([ord(char) for char in substr])
            
            if asc1 == substr_asc:
                candidates.append(substr)
            
        for c in candidates:
            if counterS1 == Counter(c):
                return True
            

        return False 
        
        