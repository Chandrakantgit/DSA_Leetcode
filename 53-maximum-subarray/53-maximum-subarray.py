class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = nums[0]
        sumo = 0
        for x in nums:
            sumo= sumo + x
            if sumo > maximum :
                maximum = sumo
            if sumo < 0:
                sumo = 0
        return maximum
        