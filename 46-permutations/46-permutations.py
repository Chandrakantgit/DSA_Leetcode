class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
#         More optimized solution 

#         def recurPermute(ind,arr,ans):
#             if ind ==  len(arr):
#                 ar = list()
#                 for x in arr:
#                     ar.append(x)
#                 ans.append(ar)
#                 return
#             for j in range(ind,len(nums)):
#                 arr[ind],arr[j] = arr[j],arr[ind]
#                 recurPermute(ind+1,arr,ans)
#                 arr[ind],arr[j]=arr[j],arr[ind]
                
#         def caller(num):
#             ans = list()
#             recurPermute(0,num,ans)
#             return ans
            
#         return caller(nums)


        def recurPermute(ds,arr,ans,freq):
            if len(ds) ==  len(arr):
                ar = list()
                for x in ds:
                    ar.append(x)
                ans.append(ar)
                return
            for j in range(0,len(nums)):
                if not freq[j]:
                    freq[j]=True
                    ds.append(nums[j])
                    recurPermute(ds,arr,ans,freq)
                    ds.pop()
                    freq[j]=False
                
        def caller(num):
            ans = list()
            freq = [False]*len(nums)
            recurPermute([],num,ans,freq)
            return ans
            
        return caller(nums)

