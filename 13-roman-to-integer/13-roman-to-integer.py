class Solution:
    def romanToInt(self, s: str) -> int:
        stak = list()
        current = 0
        for x in s:
            if stak == []:
                stak.append(x)
                if x == "I":
                    current+=1
                elif x == "V":
                    current +=5
                elif x == "X":
                    current += 10
                elif x == "L":
                    current += 50
                elif x == "C":
                    current += 100
                elif x == "D":
                    current += 500
                elif x == "M":
                    current += 1000
            else:
                
                
                if stak[-1] == "I" and (x == "V" or x=="X"):
                    temp = ""
                    try:
                        while stak[-1] == "I":
                            temp+=stak.pop()
                    except:
                        pass
                    if x == "V":
                        current += 5 - (1*len(temp)*2)
                    else:
                        current += 10 - (1*len(temp)*2)
                        
                        
                elif stak[-1] == "X" and (x == "L" or x=="C"):
                    temp = ""
                    try:
                        while stak[-1] == "X":
                            temp+=stak.pop()
                    except:
                        pass
                    if x == "L":
                        current += 50 - (10*len(temp)*2)
                    else:
                        current += 100 - (10*len(temp)*2)
                        
                        
                elif stak[-1] == "C" and (x == "D" or x=="M"):
                    temp = ""
                    try :
                        while stak[-1] == "C":
                            temp+=stak.pop()
                    except:
                        pass
                    if x == "D":
                        current += 500 - (100*len(temp)*2)
                    else:
                        current += 1000 - (100*len(temp)*2)
                else:
                    stak.append(x)
                    if x == "I":
                        current+=1
                    elif x == "V":
                        current +=5
                    elif x == "X":
                        current += 10
                    elif x == "L":
                        current += 50
                    elif x == "C":
                        current += 100
                    elif x == "D":
                        current += 500
                    elif x == "M":
                        current += 1000
                    
        return current
                
                        
            
        