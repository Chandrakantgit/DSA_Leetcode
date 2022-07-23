class Solution:
    
            
    
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        arr,ans = sorted(nums),[]
        for num in nums:
            
            i = bisect_left(arr,num)    
            ans.append(i)               
            del arr[i]                  
            
        return ans                    
        
        
        
        
        
        
        
        
        
        # Brute force approach (didn't work)
        
        # ans = [0]*len(nums)
        # for x in range(len(nums)-1,-1,-1):
        #     if x == len(nums)-1:
        #         ans[x]=0
        #     else:
        #         count = 0
        #         for i in range(x,len(nums)):
        #             if nums[x] > nums[i]:
        #                 count+=1
        #             else:
        #                 pass
        #         ans[x]=count
        # return ans
        