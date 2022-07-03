class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        flag = False
        ans = [nums[0]]
        temp = nums[0]
        for x in nums[1:]:
            if flag == False and x > temp:
                ans.append(x)
                flag = True
                temp = x
            elif flag == True and x < temp:
                ans.append(x)
                flag = False
                temp = x
            else:
                temp = x
        
        temp = nums[0]
        ans1=[nums[0]]
        flag = False
        for x in nums[1:]:
            if flag == False and x < temp:
                ans1.append(x)
                flag = True
                temp = x
            elif flag == True and x > temp:
                ans1.append(x)
                flag = False
                temp = x
            else:
                temp = x
        if len(ans) > len(ans1):
            return len(ans)
        else:
            return len(ans1)
                
        