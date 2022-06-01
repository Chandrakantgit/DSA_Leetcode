class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        arr = []
        sum = 0
        for x in range(len(nums)):
            if arr == []:
                sum=nums[x]+0
                arr.append(sum)
            else:
                sum = nums[x] + arr[-1]
                arr.append(sum)
        return arr