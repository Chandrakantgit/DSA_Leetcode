class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        max_h = 0 
        max_w = 0
        verticalCuts = sorted(verticalCuts)
        horizontalCuts = sorted(horizontalCuts)
        
        for x in range(len(verticalCuts)):
            temp_w = 0
            if x==0 and verticalCuts[x] != 0:
                temp_w = verticalCuts[x] - 0
                if temp_w > max_w:
                    max_w = temp_w
            elif x==0 and verticalCuts[x] ==0:
                pass
            else:
                temp_w = verticalCuts[x]-verticalCuts[x-1]
                if temp_w > max_w:
                    max_w = temp_w
                else:
                    pass
        if w - verticalCuts[x] > max_w:
            max_w = w - verticalCuts[x]
                
        for y in range(len(horizontalCuts)):
            temp_h = 0
            if y==0 and horizontalCuts[y] != 0:
                temp_h = horizontalCuts[y] - 0
                print("here",temp_h)
                if temp_h > max_h:
                    max_h = temp_h
            elif y ==0 and horizontalCuts[y]==0:
                pass
            else:
                temp_h = horizontalCuts[y]- horizontalCuts[y-1]
                print("here1",temp_h)
                if temp_h > max_h:
                    max_h = temp_h
                else:
                    pass
        print(max_h,max_w)
        if h - horizontalCuts[y] > max_h:
            max_h = h -  horizontalCuts[y]
            
        return (max_h*max_w)%(10**9+7)
            
                
        