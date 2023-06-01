class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 잘라서 처리하는 것은 안 될 것 
        # 수로 바꾸는 방법도 생각해볼것
        
        # 탐색 자체는 python in을 활용하면 탐색할 수 있음 
        
        # 문제는 permutation 경우의수 완전탐색하는 건데 
        # 1 trie를 쓴다
        # 2 sliding window를 쓴다 
        
        # 1 길이만큼 자른다 window를 만들고
        # * 먼저 등장하면 true로 quite 
        
        
        len1 = len(s1)
        len2 = len(s2)

        counterS1 = Counter(s1)
        
        for i in range(len2-len1+1): 
            substr = s2[i: i+len1]
            if counterS1 == Counter(substr):
                return True
        
        return False 
        
        