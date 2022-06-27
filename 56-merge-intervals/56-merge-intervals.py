class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        print(intervals)
        ans = []
        pair = intervals[0]
        for x in intervals:
            if x[0] <= pair[1]:
                pair[0] = min(pair[0],x[0])
                pair[1] = max(pair[1],x[1])
                print(pair)
            else:
                ans.append(pair)
                pair = x
        if pair not in ans:
            ans.append(pair)
        return ans
                
            
                    
            
                    
        