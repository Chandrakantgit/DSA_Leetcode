class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        def f(ind,arr):
            if ind >= len(nums):
                ar = []
                ar.extend(arr)
                output.append(ar)
                return
            arr.append(nums[ind])
    
            f(ind+1,arr)
            arr.pop()
            f(ind+1,arr)

        def ma():
            f(0,[])

        ma()
        return output
        