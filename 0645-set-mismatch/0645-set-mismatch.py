class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        arr = []
        for u in range(0,len(nums)+1):
            arr.append(0)
        for x in nums:
            arr[x]+=1
        
        replaced = 0
        wReplaced = 0
        for y in range(1,len(nums)+1):
            if arr[y] ==2:
                wReplaced = y
            if arr[y] == 0:
                replaced = y
        return [wReplaced,replaced]