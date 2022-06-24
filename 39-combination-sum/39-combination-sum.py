class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        answer = list()
        self.findCombination(0,candidates, target , answer ,[])
        return answer
          
        
    def findCombination(self,ind , arr , targ , answer ,ds):
        
        if ind == len(arr):
            if targ == 0:
                ar = list()
                ar = [x for x in ds]
                answer.append(ar)
            return
        
        if arr[ind] <= targ :
            ds.append(arr[ind])
            self.findCombination(ind,arr,targ-arr[ind],answer,ds)
            ds.pop()
            
        self.findCombination(ind+1,arr,targ,answer,ds)
        
        
        