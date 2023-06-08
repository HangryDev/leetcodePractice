class Solution:
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        l, r = 1, max(piles)
        while l < r:
            m = l + (r-l) // 2
            time = sum([math.ceil(i/m) for i in piles])
            if time > H:
                l = m + 1
            else:
                r = m
        return l
        # 2 k를 piles[1], 그 다음 값으로 해본다. 
        # 2-1 될 경우 [2]도 
        # 2-2 안 될 경우, 전 값과 현 값의 사이를 찾아보면 되겠네. 
        # 3. 이때 하나씩 올리지 말고, 수학적으로 올리면 바이너리 서치가 될듯 
            
        
        # 작아질 수 있는 가능성을 근사하게 찾아본다
        # sum (ceil(piles / k))
        

        
        
        
        
        
        # piles = [7,3,2,4,5]
        # k = 시간당 k개의 바나나를 먹을수 있다
        # 코코는, 바나나 더미가 하나 끝나면, 그 시간(hour)동안은 바나나를 더 안먹어요
        # k가 10이든 100이든, 93개 더 먹을수 있어도 안먹는다는거죠. 
        
        # H가 이제 가드들이 돌아오는 시간이고 = 코코한테 주어진 시간 
        # 그 안에 저 piles를 다 해치워야되는데 
        # 한 더미를 끝내면 쉬니까, 최소한 len(piles)의 길이보다는 k가 커야된다
        
        
        
        
        # 이때 k의 최소값을 구하시고 
        
        
        
        
        # [300,110,230,40,200] / 230 -> [2,1,1,1,1] sum 6 == h=6 
        # [300,110,230,40,200] / 200 -> [2,1,2,1,1] sum 7 > h = 6 
        
        # 200 ~ 230 -> 215, 222, 218, 216 
        # left = 200 
        # right = 230 
        # mid = left+right/2
         
        
        
        
        
        
        