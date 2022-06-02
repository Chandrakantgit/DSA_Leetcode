class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        if len(matrix) == len(matrix[0]):
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if i<=j:
                        pass
                    else:
                        matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
            return matrix
        else:
            r = len(matrix)
            c = len(matrix[0])
            arrr= []
            
            for x in range(c):
                arrr.append([])
            
            for i in range(c):
                for j in range(r):
                    arrr[i].append(matrix[j][i])
            return arrr
        
    