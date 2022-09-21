class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        evenSum = 0
        for x in nums:
            if x%2 ==0:
                evenSum += x
        print(evenSum)
        ans = []
        for a in queries:
            
            if nums[a[1]] % 2 ==0:
                temp = nums[a[1]] + a[0]
                print("here temp",temp,nums[a[1]])
                
                if temp < nums[a[1]] and temp %2 ==0:
                    evenSum -= (nums[a[1]] - temp)
                    nums[a[1]] = temp
                    print(temp,1)
                    ans.append(evenSum)
                elif temp >= nums[a[1]] and temp %2 ==0:
                    evenSum += (temp - nums[a[1]])
                    nums[a[1]] = temp
                    print(temp,2)
                    ans.append(evenSum)
                else:
                    evenSum -= nums[a[1]]
                    nums[a[1]] = temp
                    print(temp,3)
                    ans.append(evenSum)  
            else:
                temp = (nums[a[1]]) + (a[0])
                if temp %2 == 0:
                    evenSum += temp
                    nums[a[1]] = temp
                    print(temp,4)
                    ans.append(evenSum)
                else:
                    nums[a[1]] = temp
                    ans.append(evenSum)
        return ans
                    
                
                
        