class Solution(object):
    def imageSmoother(self, img):
        # list 초기화. i*i의 2차원 
        #cnvl = [[0,0,0],[0,0,0],[0,0,0]]
         
        # 1-1 j가 플러스 될 때마다, 각 2차원 list의 마지막 element를  뺌. 
        # 1-2 i가 플러스 될 때마다, 1차원의 첫 list를 빼고, j는 반대 방향으로 이동함. 
        
        # 2 floor(sum(cnvl)) / sum(boolean(cnvl))) 
        m, n = len(img), len(img[0])
        res = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                res[i][j] = self.smoothen(img, i, j)

        return res

    def smoothen(self, img, x, y):
        m, n = len(img), len(img[0])
        _sum, count = 0, 0

        for i in range(-1, 2):
            for j in range(-1, 2):
                nx, ny = x + i, y + j
                if 0 <= nx < m and 0 <= ny < n:
                    _sum += img[nx][ny]
                    count += 1

        return _sum // count