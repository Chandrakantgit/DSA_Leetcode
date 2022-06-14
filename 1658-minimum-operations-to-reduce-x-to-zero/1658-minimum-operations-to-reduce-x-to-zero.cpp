class Solution {
public:
    int minOperations(vector<int>& nums, int x) {
        unordered_map<int,int> map1;
        int sum=0,ans=INT_MIN,ind;
        int numsSum = accumulate(nums.begin(),nums.end(),0);
        int perfectSubArraySum = numsSum-x;
        if(perfectSubArraySum==0) return nums.size();
        map1[0]=-1;
        for(int i=0;i<nums.size();i++)
        {
            sum+=nums[i];
            if(map1.find(sum-perfectSubArraySum)!=map1.end())
            {
                ind=map1[sum-perfectSubArraySum];
                ans=max(ans,i-ind);
            }
            map1[sum]=i;
        }
        if(ans==INT_MIN) return -1;
        return nums.size()-ans;
    }
};

// class Solution:
//     def minOperations(self, nums: List[int], x: int) -> int:
//         start = 0 
//         end = 0
//         len_arr = 0
//         cur_sum = 0
//         fullSum = 0
//         maxlen =0
//         d = dict()
//         d[0] = 0
        
        
//         for j in nums:
//             fullSum += j
//         k = fullSum - x
        
//         for y in range(len(nums)):
//             cur_sum += nums[y]
            
//             if cur_sum - k == 0:
//                 maxlen = y+1
//             if cur_sum - k in d.keys():
//                 start = d[cur_sum-k] 
//                 end = y+1
//                 len_arr = end - start
//                 if len_arr > maxlen:
//                     maxlen = len_arr
//             d[cur_sum] = y+1
//         if maxlen == 0:
//             return -1
//         else:
//             return len(nums) - maxlen
        