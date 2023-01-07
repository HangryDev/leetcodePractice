class Solution:
    def romanToInt(self, s: str) -> int:
        # 1 찾아서 pop하기. 
        # 특수 - IV, IX, XL, XC, CD, CM << 두개씩 세야 함
        # 나머지는 COUNT로 처리 = n^2 
        
        # 2 왼쪽부터 처리 (~2n)
        # 2-1 왼쪽부터 하나씩 처리
        # I,X,C가 나오면 2개 봄. 
        ### 마지막이라 한개거나, 특수에 해당 안하면 그냥 pop해서 처리 
        
        sp = ["CM", "CD", "XC", "XL", "IX", "IV"]
        spv = [900, 400, 90, 40, 9, 4]
        nrm = ["M", "D", "C", "L", "X", "V", "I"]
        nrmv = [1000,500,100,50,10,5,1]
        
        total = 0
        
        while s: 
            pointer = s[0]
            s = s[1:]
            if len(s) != 0 and pointer + s[0] in sp :
                total += spv[sp.index(pointer + s[0])]
                s = s[1:]
            else: 
                total += nrmv[nrm.index(pointer)]
                
        return total
        
        
        