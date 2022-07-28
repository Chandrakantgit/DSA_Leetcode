class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        Ana = dict()
        Tana = dict()
        for x in s:
            Ana[x]= Ana.get(x,0)+1
            
        for y in t:
            Tana[y] = Tana.get(y,0) +1
            
        if Ana == Tana:
            return True
        else:
            return False
            
            
        