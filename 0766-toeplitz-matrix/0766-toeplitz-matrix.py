class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]])->bool:
        rows,colms = len(matrix),len(matrix[0])
        
        for row in range (1,rows):
            for col in range (1,colms):
                if matrix[row][col]!=matrix[row-1][col-1]:
                    return False
        return True
                    
            