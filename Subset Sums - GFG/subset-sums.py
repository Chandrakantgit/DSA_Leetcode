#User function Template for python3
class Solution:
    
    def func(self,ind,sum,arr,N,ans):
        # base case
        if ind == N:
            ans.append(sum)
            return
        
        # Left recursion
        self.func(ind+1,sum + arr[ind],arr,N,ans)
        
        #Right recursion
        self.func(ind+1,sum,arr,N,ans)
        
	def subsetSums(self, arr, N):
	    ans = []
	    self.func(0,0,arr,N,ans)
	    return sorted(ans)
	    
	    
		# code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.subsetSums(arr, N)
        ans.sort()
        for x in ans:
            print(x,end=" ")
        print("")

# } Driver Code Ends