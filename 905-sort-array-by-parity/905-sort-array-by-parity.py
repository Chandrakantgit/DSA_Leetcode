class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i,j =0,0
        if len(nums) ==1:
            return nums
        while j < len(nums):
            if nums[i]%2 == 1:
                if nums[j]%2 ==0:
                    nums[i],nums[j] = nums[j],nums[i]
                    i+=1
                    j+=1
                else:
                    j+=1
            else:
                if i ==j :
                    i+=1
                    j+=1
                else:
                    i+=1
        return nums