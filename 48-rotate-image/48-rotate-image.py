class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        if row == col:
            for x in range(row):
                for y in range(x+1,col):
                    matrix[x][y],matrix[y][x] = matrix[y][x],matrix[x][y]
        for i in range(row):
            a = 0
            b = col-1
            while a <= b:
                matrix[i][a],matrix[i][b] = matrix[i][b],matrix[i][a]
                a+=1
                b-=1
                
            
                
            
        
            