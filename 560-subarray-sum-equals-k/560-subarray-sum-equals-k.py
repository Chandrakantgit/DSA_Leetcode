class Solution:
    # def subarraySum(self, nums: List[int], k: int) -> int:
#         s = set()
#         sum_ = 0
#         count = 0
#         for x in nums:
#             sum_ += x  
#             if sum_ - k == 0:
#                 count+=1
#                 print("done",x)
                 
#             if (sum_ - k) in s:
#                 count +=1
#                 print("done2",x)
#             s.add(sum_)
#         print(s)
#         return count


    def subarraySum(self, nums: List[int], k: int) -> int: 
        res = 0
        curSum = 0
        prefixSums = { 0 : 1 }
        
        for n in nums:
            curSum += n
            diff = curSum - k
            res += prefixSums.get(diff, 0)
            prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)
            
        return res
        
                
            
        