class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        bigDict = {}
        result = []
        for word in strs:
            sorted_chars = sorted(word)
            sorted_string = ''.join(sorted_chars)
            
            if sorted_string not in bigDict:
                bigDict[sorted_string] = [word]
            else:
                bigDict[sorted_string].append(word)   

        
        return bigDict.values()
        
        #1 strs의 각 words를 sort한다. 
        #2 1의 dict를 key로, value를 word로 하는 bigdict에 넣는다. { ["bat"]}
        #3 strs에 대해 1-2 반복 
        #4 bigDict의 value를 리스트로 출력한다. 
        #o(n) 
        
        