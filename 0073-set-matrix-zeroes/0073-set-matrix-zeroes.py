class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        hasZero = False
        columns = set()
        for i in range(len(matrix)):
            for point in range(len(matrix[0])):
                if matrix[i][point] == 0 :
                    columns.add(point)
                    hasZero = True
            if hasZero: 
                matrix[i] = [0]*len(matrix[0])
            hasZero = False 
        
        for row in matrix:
            for i in columns:
                row[i] = 0       
                
                    
        
        # for문 돌리면서 0을 찾아냄 
            # 0이 들어갈 column 값을 어디 저장해둔다. (복수일 수 있음)
            # 그 다음  row 전체를 바꾼다 
        
        