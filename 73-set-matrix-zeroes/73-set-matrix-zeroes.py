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
# Approach 2   Intuition: Instead of traversing through each row and column, we can use dummy arrays to check if the particular row or column has an element 0 or not, which will improve the time complexity.

# Approach:Take two dummy array one of size of row and other of size of column.Now traverse through the array.If matrix[i][j]==0 then set dummy1[i]=0(for row) and dummy2[j]=0(for column).Now traverse through the array again and if dummy1[i]==0  || dummy2[j]==0 then arr[i][j]=0,else continue.