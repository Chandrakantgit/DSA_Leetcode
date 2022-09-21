class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        evenSum = 0
        for x in nums:
            if x%2 ==0:
                evenSum += x
        ans = []
        for a in queries:
            
            if nums[a[1]] % 2 ==0:
                temp = nums[a[1]] + a[0]
                
                if temp < nums[a[1]] and temp %2 ==0:
                    evenSum -= (nums[a[1]] - temp)
                    nums[a[1]] = temp
                    ans.append(evenSum)
                elif temp >= nums[a[1]] and temp %2 ==0:
                    evenSum += (temp - nums[a[1]])
                    nums[a[1]] = temp
                    ans.append(evenSum)
                else:
                    evenSum -= nums[a[1]]
                    nums[a[1]] = temp
                    ans.append(evenSum)  
            else:
                temp = (nums[a[1]]) + (a[0])
                if temp %2 == 0:
                    evenSum += temp
                    nums[a[1]] = temp
                    ans.append(evenSum)
                else:
                    nums[a[1]] = temp
                    ans.append(evenSum)
        return ans
                    
                
                
        