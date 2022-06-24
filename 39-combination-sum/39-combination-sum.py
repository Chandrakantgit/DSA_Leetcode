class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        answer = list()
        self.findCombination(0,candidates, target , answer ,[])
        return answer
          
        
    def findCombination(self,ind , arr , targ , answer ,ds):
        
        if ind == len(arr):
            if targ == 0:
                ar = list()                     #This pasrt here what is does ??
                ar = [x for x in ds]            # see if you directly copy the ds in answer,every element in answer would be same list 
                answer.append(ar)               # and every operation done on that list would refelct on every element in answer
            return                              # so at last the answer is going to be empty arrays
        
        if arr[ind] <= targ :
            ds.append(arr[ind])
            self.findCombination(ind,arr,targ-arr[ind],answer,ds)
            ds.pop()
            
        self.findCombination(ind+1,arr,targ,answer,ds)
        
        
        