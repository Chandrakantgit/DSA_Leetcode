class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        matrix = []
        for r in range(numRows):
            arr = list()
            if r == 0:
                arr = [0]*(r+1)
                arr[0] = 1
            elif r == 1:
                arr = [0]*(r+1)
                arr[0]=1
                arr[-1]=1
            else:
                arr = [0]*(r+1)
                arr[0]=1
                arr[-1]=1
                for j in range(1,r):
                    arr[j] = matrix[r-1][j-1]+matrix[r-1][j]   
            matrix.append(arr)
        return matrix
                