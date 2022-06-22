class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def recurPermute(ind,arr,ans):
            if ind ==  len(arr):
                ar = list()
                for x in arr:
                    ar.append(x)
                ans.append(ar)
                return
            for j in range(ind,len(nums)):
                arr[ind],arr[j] = arr[j],arr[ind]
                recurPermute(ind+1,arr,ans)
                arr[ind],arr[j]=arr[j],arr[ind]
                
        def caller(num):
            ans = list()
            recurPermute(0,num,ans)
            return ans
            
        return caller(nums)