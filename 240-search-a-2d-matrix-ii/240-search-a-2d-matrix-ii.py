class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        i = 0
        j = 0
        flag = 0
        while i < m:
            for x in range(n):
                if matrix[i][x] == target:
                    return True
                elif matrix[i][x] > target:
                    n=x
                    break
            i+=1
                        
        
        