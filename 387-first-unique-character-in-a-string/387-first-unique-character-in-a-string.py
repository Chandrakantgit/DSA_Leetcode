class Solution:
    def firstUniqChar(self, s: str) -> int:
        dec = dict()
        for x in s:
            dec[x] = dec.get(x,0) + 1
            
        for y in range(0,len(s)):
            if dec.get(s[y],0)  == 1:
                return y
        return -1
        