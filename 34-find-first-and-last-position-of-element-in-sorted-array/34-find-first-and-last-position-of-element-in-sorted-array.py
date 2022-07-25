class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binSearch(target,nums,True)
        right = self.binSearch(target,nums,False)
        return [left,right]
        ## Clearly its an easy question for O(n) solution but it tkaes a turn when asked to be implemented in O(logn). Clearly Binary 
        
    
    def binSearch(self,target,nums,leftbias):
        l,r=0,len(nums)-1
        i = -1
        while l<=r:
            m = (l+r)//2
            if nums[m] > target:
                r = m-1
            elif nums[m] < target:
                l = m+1
            else:
                i = m 
                if leftbias:
                    r=m-1
                else:
                    l=m+1
        return i 
        
        