class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        l = 0
        r = len(height)-1
        max_water = 0
        while l < r :
            temp_water = (r-l) * min(height[l],height[r])
            if temp_water > max_water :
                max_water = temp_water
                
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        return max_water
            
                
#         area =0
#         ass = len(height)
#         for x in range(ass):
#             for y in range(x+1,ass):
#                 ar = min(height[x],height[y]) * (y-x)
#                 if ar > area:
#                     area = ar
                    
#         return area

          
        
            
        