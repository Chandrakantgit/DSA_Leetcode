import sys
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        
        # for x in range(n-1,0,-1):
        #     temp = nums[x]
        #     for y in range(x-1,-1,-1):
        #         if nums[y] < temp:
        #             for j in range(y-1,-1,-1):
        #                 if nums[j] < nums[y]:
        #                     return True
        # return False
        # Toooo complex
        
        if n < 3:
            return False
        
        left = sys.maxsize
        mid = sys.maxsize
        for x in nums:
            
            if x > mid:
                return True
            elif x > left and x < mid:
                mid = x
            elif x < left:
                left = x
                
        return False
            
        