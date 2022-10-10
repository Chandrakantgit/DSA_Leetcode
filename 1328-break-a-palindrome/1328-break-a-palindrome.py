class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        
        n = len(palindrome)
        if n == 1:
            return ''
        
        l,r = 0,n-1
        flag = False
        
        while l < r and not flag:
            print(palindrome[l])
            if palindrome[l] != "a":
                palindrome = palindrome[:l]+"a"+palindrome[l+1:]
                flag = True
            l+=1
            r-=1
            
        if not flag:
            palindrome = palindrome[:n-1] + "b"
            
        return palindrome
        