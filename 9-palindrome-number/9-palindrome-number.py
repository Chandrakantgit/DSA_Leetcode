class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp2 = pow(2,31)
        if ((0 <= x) and (x < temp2)): 
            string=str(x)
            strng=string[::-1]
            if (string == strng):
                return True
            else:
                return False