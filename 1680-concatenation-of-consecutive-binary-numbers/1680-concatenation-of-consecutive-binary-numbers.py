class Solution:
    def concatenatedBinary(self, n: int) -> int:
        s = ""
        for x in range(1,n+1):
            s+=str(bin(x)[2:])
        ans = int(s,2)
        return ans%(10**9 + 7)
            