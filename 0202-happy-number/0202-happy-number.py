class Solution:
    def isHappy(self, n: int) -> bool:
        number = str(n)
        
        for j in range(1,100):
            newnumber = 0 
            for i in str(number):
                newnumber += (int(i))**2
            number = newnumber
            if number == 1:
                return True
        
        return False