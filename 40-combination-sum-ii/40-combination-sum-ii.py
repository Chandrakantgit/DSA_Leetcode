class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates = sorted(candidates)
        self.FindCombinations(0,candidates,target,[],ans)
        return ans
        
        
        
    def FindCombinations(self,ind, arr, target ,ds , ans):
        
        if target == 0:
            d = [x for x in ds]
            ans.append(d)
            return 
         
        for y in range(ind,len(arr)):
            if y > ind and arr[y] == arr[y-1] :
                continue
            if arr[y] > target:
                break
                
            ds.append(arr[y])
            self.FindCombinations(y+1,arr,target - arr[y],ds ,ans)
            ds.pop()
            
            
        