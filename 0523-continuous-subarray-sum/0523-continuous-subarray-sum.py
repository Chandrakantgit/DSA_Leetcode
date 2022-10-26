# class Solution:
#     def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
#         Sum = sum(nums)
#         if len(nums)==1:
#             return False
#         if Sum % k == 0:
#             return True
#         left = 0
#         right = len(nums)-1
#         while left != right:
#             print(Sum)
#             elif Sum % k == 0:
#                 return True
#             elif (Sum - nums[left]) % k == 0 or (Sum - nums[right]) % k == 0:
#                 return True
#             else:
#                 Sum -= nums[left]
#                 Sum -= nums[right]
#                 left +=1
#                 right -=1

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d , s = {0:-1} , 0
        for i, n in enumerate(nums):
            if k != 0:
                s = (s + n) % k
            else:
                s += n
            if s not in d:
                d[s] = i
            else:
                if i - d[s] >= 2:
                    return True
        return False
            
        