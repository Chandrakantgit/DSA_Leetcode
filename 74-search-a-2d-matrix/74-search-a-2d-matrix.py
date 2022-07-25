class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        i = 0
        j=  n-1
        while j >-1 and i < m:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j-=1
            elif matrix[i][j] < target:
                i+=1
                
        else:
            return False
        