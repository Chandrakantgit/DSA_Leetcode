class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        Hashset = {}
        for x in nums:
            Hashset[x] = 1
            
        max_len = 0
        for y in nums:
            if Hashset.get(y-1,0) >=1:
                pass
            else:
                k = y
                temp = True
                temp_len = 1
                while temp:
                    if Hashset.get(k+1,0) >= 1:
                        k+=1
                        temp_len+=1
                        pass
                    else:
                        temp = False
                if max_len < temp_len:
                    max_len = temp_len
        return max_len
                        
                
            