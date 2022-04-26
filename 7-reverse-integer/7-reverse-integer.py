class Solution:
    def reverse(self, x: int) -> int:
        # Variables
        sol = ""
        string = str(x)
        #if x is negitive make sure the sol is negetive
        if string[0] == "-":
            sol+="-"
        # itreating over str and appending every char to sol in backwords order
        for i in string[::-1]:
            #if we find negetive dont do anything cause we alreadyu have apended it
            if i == "-":
                continue
            sol+=i
        # Not really needed for the range
        temp = pow(-2, 31)
        temp2 = pow(2,31) - 1      
        #if the sol is out of range
        if int(sol) not in range(temp, temp2):
            return 0
           
        return(int(sol))
    