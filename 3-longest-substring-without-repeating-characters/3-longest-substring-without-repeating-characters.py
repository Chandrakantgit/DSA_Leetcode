class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)>0:
            longest = s[0]
        else:
            return 0
        for i in range(0,len(s)):
            temp = s[i]
            for j in range(i+1,len(s)):
                if s[j] in temp:
                    break
                else:
                    temp = temp + s[j]
            if len(temp) > len(longest):
                longest = temp
        return len(longest)
                    
                
        