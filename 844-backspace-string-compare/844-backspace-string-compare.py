class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 =[]
        stack2 =[]
        for x in s:
            try:
                if x != "#":
                    stack1.append(x)
                else:
                    stack1.pop()
            except:
                pass
        for y in t:
            try:
                if y != "#":
                    stack2.append(y)
                else:
                    stack2.pop()
            except:
                pass
                
        return stack1 == stack2
        
        
            
        