class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        #while문으로 접근하는게 좋겠군 
            #1번: 제일 처음 row를 팝하고. 
            #2번: range(0,len(matrix),1)번 반복/ matrix[i][-1]을 가져옴
            #3번: 제일 마지막 row를 pop하고 reverse
            #4번: range(len(matrix),0,-1)로 역순, matrix[i][0]
        
        output = []        
        while matrix:
            output.extend(matrix.pop(0))
            if matrix == []: 
                break
            print(matrix)
            for i in range(0,len(matrix),1):
                output.append(matrix[i].pop(-1))
            matrix = [x for x in matrix if x]
            print(matrix)
            if matrix == []: 
                break
            row = matrix.pop()
            row.reverse()
            output.extend(row)
            print(matrix)
            if matrix == []: 
                break
            for i in range(len(matrix)-1,-1,-1):
                output.append(matrix[i].pop(0))
            matrix = [x for x in matrix if x]
            
            
            
        
        return output