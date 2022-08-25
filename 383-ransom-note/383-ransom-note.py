class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a = dict()
        b = dict()
        for x in ransomNote:
            a[x]= a.get(x,0)+1
        for y in magazine:
            b[y]= b.get(y,0)+1
        for e in ransomNote:
            try:
                if a[e] > b[e]:
                    return False
            except:
                return False
        return True
                
        
        