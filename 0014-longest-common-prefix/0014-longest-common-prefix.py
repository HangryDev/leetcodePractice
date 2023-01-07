class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs.pop(0)
        
        while strs:
            pointer = strs.pop(0)
            ranges = min(len(prefix),len(pointer))

            for i in range(0,ranges):
                if prefix[i] == pointer[i]:
                    pass
                else: 
                    prefix = prefix[0:i]
                    break;
            else:
                prefix = prefix[0:ranges]
                    
        return prefix
        
        