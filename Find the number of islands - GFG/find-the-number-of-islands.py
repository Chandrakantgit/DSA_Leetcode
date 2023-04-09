#User function Template for python3

import sys
sys.setrecursionlimit(10**8)
class Solution:

    def bfs(self,r,c,grid,visited):
        visited[r][c] = True
        queue = []
        queue.append((r,c))
        lr = len(grid)
        lc = len(grid[0])

        while queue != []:
            i = queue[0][0]
            j = queue[0][1]
            queue.pop(0)
            

            for x in range(-1,2):
                for y in range(-1,2):
                    nrow = i+x
                    ncol = j+y
                    
                    if nrow >= 0 and ncol >= 0 and ncol < lc and nrow < lr and visited[nrow][ncol] == False and grid[nrow][ncol]==1:
                        queue.append((nrow,ncol))
                        visited[nrow][ncol] = True

    def numIslands(self, grid):
        n = len(grid)
        m = len(grid[0])
        visited  = []
        for x in range(n):
            visited.append([False]*m)
        count = 0
        for i in range(n):
            for j in range(m):
                

                if (visited[i][j] == False) and grid[i][j]==1:
                    self.bfs(i,j,grid,visited)
                    
                    count = count + 1
        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n,m=map(int,input().strip().split())
        grid=[]
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        obj=Solution()
        print(obj.numIslands(grid))
# } Driver Code Ends