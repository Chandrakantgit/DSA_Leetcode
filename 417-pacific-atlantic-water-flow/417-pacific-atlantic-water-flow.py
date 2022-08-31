class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
#         m = len(heights)
#         n = len(heights[0])
#         ans = []
        
#         if heights == None or len(heights)==0 or len(heights[0]) ==0:
#             return ans
        
#         pacific = [[False]*m]*n
#         atlantic = [[False]*m]*n
        
#         for j in range(n):
#             self.dfs(0,j,pacific,heights,-1)
#             self.dfs(m-1,j,atlantic,heights,-1)
#         for i in range(m):
#             self.dfs(i,0,pacific,heights,-1)
#             self.dfs(i,n-1,atlantic,heights,-1)
        
        
#         print(pacific)
#         print(atlantic)
#         for a in range(0,m):
#             for b in range(0,n):
#                 if pacific[a][b] and atlantic[a][b]:
#                     arr = list()
#                     arr.append(a)
#                     arr.append(b)
#                     ans.append(arr)
        
#         return ans
                    
                
#     def dfs(self,i,j,canReach,heights,prevHeight):
#         try:
#             if (i < 0) or (j < 0) or (i > len(heights)) or (j > len(heights[0])) or canReach[i][j] or heights[i][j] < prevHeight:
#                 return
#         except:
#             return
#         print(canReach)
#         canReach[i][j] = True
#         print(canReach)
        
#         self.dfs(i+1,j,canReach,heights,heights[i][j])
#         self.dfs(i-1,j,canReach,heights,heights[i][j])
#         self.dfs(i,j-1,canReach,heights,heights[i][j])
#         self.dfs(i,j+1,canReach,heights,heights[i][j])

        m, n = len(heights), len(heights[0])
        
        def dfs(i: int, j: int, prev_height: int, coords: Set[Tuple[int]]) -> None:
            if i < 0 or i == m or j < 0 or j == n:
                # out of bounds
                return
            
            if (i, j) in coords:
                # already visited
                return
            
            height = heights[i][j]
            
            if height < prev_height:
                # water can't flow to a higher height
                return
            
            # ocean is reachable from current coordinate
            coords.add((i, j))
            
            # all four directions
            dfs(i + 1, j, height, coords)
            dfs(i - 1, j, height, coords)
            dfs(i, j + 1, height, coords)
            dfs(i, j - 1, height, coords)
            
        pacific_coords = set()
        
        # top row
        for j in range(n):
            dfs(0, j, 0, pacific_coords)
        
        # left col
        for i in range(m):
            dfs(i, 0, 0, pacific_coords)
            
        atlantic_coords = set()
            
        # right col
        for i in range(m):
            dfs(i, n - 1, 0, atlantic_coords)
            
        # bottom row
        for j in range(n):
            dfs(m - 1, j, 0, atlantic_coords)
            
        # intersection of coords reachable from both Pacific and Atlantic
        return list(pacific_coords & atlantic_coords)
        
        