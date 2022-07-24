class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #This is Brute force approach
        # m = len(matrix)
        # n = len(matrix[0])
        # i = 0
        # j = 0
        # flag = 0
        # while i < m:
        #     for x in range(n):
        #         if matrix[i][x] == target:
        #             return True
        #         elif matrix[i][x] > target:
        #             n=x
        #             break
        #     i+=1
        
        m = len(matrix)
        n = len(matrix[0])
        j = 0
        i = m-1
        while i >-1 and j < n:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                j+=1
            elif matrix[i][j] > target:
                i-=1
        else: return False
        
        