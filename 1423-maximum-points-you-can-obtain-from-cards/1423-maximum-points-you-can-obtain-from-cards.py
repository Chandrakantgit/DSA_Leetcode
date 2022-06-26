# class Solution:
#     def maxScore(self, cardPoints: List[int], k: int) -> int:
#         i = 0
#         m = len(cardPoints)-k
#         mini = sum(cardPoints[i:i+m])
#         temp = mini
        
#         while i + m -1 < len(cardPoints):
#             # print("i",i)
#             # print("i+m-1",i+m-1)
#             # print("temp",temp)
#             try:
#                 if temp < mini:
#                     temp = mini
#                 temp = temp - cardPoints[i] + cardPoints[i+m-1]
#                 i+=1
#             except:
#                 i+=1
#                 pass
#         return sum(cardPoints) - mini
            
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        total = sum(cardPoints)
        
        remaining_length = n - k
        subarray_sum = sum(cardPoints[:remaining_length])
        
        min_sum = subarray_sum
        for i in range(remaining_length, n):
            # Update the sliding window sum to the subarray ending at index i
            subarray_sum += cardPoints[i]
            subarray_sum -= cardPoints[i - remaining_length]
            # Update min_sum to track the overall minimum sum so far
            min_sum = min(min_sum, subarray_sum)
        return total - min_sum
        
            
        