class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ansList = []
        self.findSubset(0,nums,[],ansList)
        return ansList
    
    def findSubset(self,ind:int,nums:List[int],ds:List[int],ansList:List[List[int]]):
        tempArr =[x for x in ds]
        ansList.append(tempArr)
        for i in range(ind,len(nums)):
            if i!= ind and nums[i] == nums[i-1]: continue
            ds.append(nums[i])
            self.findSubset(i+1,nums,ds,ansList)
            ds.pop()