class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        arr = []
        sum = 0
        for x in nums:
            sum = sum + x
            arr.append(sum)
        return arr