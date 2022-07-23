class Solution:
    
            
    
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        # bisect.bisect_left(a, x, lo=0, hi=len(a), *, key=None)
# Locate the insertion point for x in a to maintain sorted order. The parameters lo and hi may be used to specify a subset of the list which should be considered; by default the entire list is used. If x is already present in a, the insertion point will be before (to the left of) any existing entries. The return value is suitable for use as the first parameter to list.insert() assuming that a is already sorted.
        
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
        