class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == None or len(strs) == 0 or strs[0] == "" : return ""
        for i in range (0, len(strs[0])):
            c = strs[0][i]
            for j in range (0, len(strs)):
                if i == len(strs[j]) or strs[j][i] != c:
                    return strs[0][0:i]
        return strs[0]
        
        