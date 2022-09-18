class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        l = len(s)
        for x in range(l-1):
            s = s[-1]+s[0:l-1]
            if s == goal:
                return True
            else:
                pass
        return False
            
            
        