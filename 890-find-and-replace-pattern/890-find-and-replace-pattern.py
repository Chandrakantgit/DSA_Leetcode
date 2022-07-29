class Solution:
    def findAndReplacePattern(self, words: List[str], p: str) -> List[str]:
        # if words == ["abcdefghijklab","abcdefghijkabl"]:
        #     return ["abcdefghijklab"]
        ans = []
        Map_p={}
        Set_p=set()
        numPattern = ""
        for x in p:
            if x in Set_p:
                numPattern = numPattern+str(Map_p[x])
            else:
                Set_p.add(x)
                Map_p[x] = Map_p.get(x,len(Set_p)-1)
                numPattern = numPattern+str(Map_p[x])
        
        for y in words:
            numPattern2 = ""
            Map_p={}
            Set_p=set()
            for z in y:
                if z in Set_p:
                    numPattern2 = numPattern2+str(Map_p[z])
                else:
                    Set_p.add(z)
                    Map_p[z] = Map_p.get(z,len(Set_p)-1)
                    numPattern2 = numPattern2+str(Map_p[z])
                    
                if numPattern2 == numPattern[0:len(numPattern2)]:
                    pass
                else:
                    break
            if numPattern == numPattern2:
                ans.append(y)
                
        return ans