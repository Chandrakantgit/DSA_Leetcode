class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # SOLUTION WITH O(N^2)
        # max_prof = 0
        # for x in range(0,len(prices)):
        #     for y in prices[x+1:]:
        #         if y - prices[x] > max_prof:
        #             max_prof = y - prices[x]
        # return max_prof
        
#         With linear time complexity
        maxSoFar = 0
        minSoFar = 10000
        for x in prices:
            minSoFar = min(minSoFar,x)
            maxSoFar = max(maxSoFar,x - minSoFar)
        return maxSoFar
        