class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        MAX = max(nums) ### Find the largest number in nums.
        res = 0			 
        count = 0		### Used to count the length of the continues subarray that only contains MAX
        for n in nums:
        	### If the current number is MAX, increase count
            if n==MAX:
                count +=1
            ### Otherwise, reset count.
            else:
                count = 0
            ### store the maximum count as result.
            res = max(res, count)
        return res