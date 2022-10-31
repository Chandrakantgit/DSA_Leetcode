class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]])->bool:
        rows,colms = len(matrix),len(matrix[0])
        
        for r in range (1,rows):
            for c in range (1,colms):
                if matrix[r][c]!=matrix[r-1][c-1]:
                    return 0
        return 1
                    
            