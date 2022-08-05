class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        
        def solveMem(num,tar,dp):
            if tar < 0:
                return 0
            if tar == 0:
                return 1
            
            if dp[tar]!=-1:
                return dp[tar]
            
            ans = 0
            for x in range(0,len(num)):
                ans += solveMem(num,tar-num[x],dp)
            
            dp[tar] = ans
            return dp[tar]
        
        dp = [-1]*(target+1)
        return solveMem(nums,target,dp)
                
        
        