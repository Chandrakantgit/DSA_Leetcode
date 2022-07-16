class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ansList = []
        self.findSubset(0,nums,[],ansList)
        return ansList
    
    
    ##Optimized form of SUbset I , Tiem complexity : 2^n * n ,Space complexity: 2^n , Auxiliary space for recursion : O (n)
    
    def findSubset(self,ind:int,nums:List[int],ds:List[int],ansList:List[List[int]]):
        tempArr =[x for x in ds]
        ansList.append(tempArr)
        for i in range(ind,len(nums)):
            if i!= ind and nums[i] == nums[i-1]: continue
            ds.append(nums[i])
            self.findSubset(i+1,nums,ds,ansList)
            ds.pop()