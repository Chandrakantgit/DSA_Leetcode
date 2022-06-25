class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # sum all values in range
        range_sum = 0
        for i in range(len(nums) + 1):
            range_sum += i
        
        # subtract every value in array from the sum
        # the leftover value is what is missing
        for i in range(len(nums)):
            range_sum -= nums[i]
        # just making it clear what we are returning  
        missing = range_sum
        return missing