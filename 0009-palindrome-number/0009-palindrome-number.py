class Solution:
    def isPalindrome(self, x: int) -> bool:
        str1 = list(str(x))
        
        #1 앞과 뒤를 매칭해본다
        #2 실패시 false 
        #3 1, 0이 될 경우 true
        
        while len(str1)>1:
            a = str1.pop(0)
            b = str1.pop(-1)
            if a !=b:
                return False
        
        return True