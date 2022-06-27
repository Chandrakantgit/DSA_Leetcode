class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # THE VERY FIRST THING TO DO IS  SORT THE QUESTION ARRAY OR LIST
        # THEN TAKE A TEMPORARY PAIR STARTING FROM FIRST ELEMENT OF SORTED ARRAY AND THEN
        # THEN ITERATE OVER  ARRAY TO CHECK WHETHER PAIR AND CURRENT PAIR COULD BE MERGED
        # IF CAN'T BE MERGED THEN YOU HAVE TO ADD THAT PAIR IN ANS ARRAY ELSE MERGE ARRAY
        
        intervals = sorted(intervals)
        ans = []
        pair = intervals[0]
        for x in intervals:
            if x[0] <= pair[1]:
                pair[0] = min(pair[0],x[0])
                pair[1] = max(pair[1],x[1])
            else:
                ans.append(pair)
                pair = x
        if pair not in ans:
            ans.append(pair)
        return ans
                
            
                    
            
                    
        