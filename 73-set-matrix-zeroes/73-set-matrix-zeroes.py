class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row = len(matrix)
        column = len(matrix[0])
        if row ==0 and column == 0:
            return 
        l = []
        for x in range(row):
            for y in range(column):
                if matrix[x][y] == 0:
                    l.append((x,y))
        for s in l:
            for t in range(column):
                matrix[s[0]][t] = 0
            for u in range(row):
                matrix[u][s[1]] = 0
        """
        Do not return anything, modify matrix in-place instead.
        """
        