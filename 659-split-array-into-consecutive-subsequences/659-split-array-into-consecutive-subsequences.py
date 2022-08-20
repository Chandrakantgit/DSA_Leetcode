class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        
        availabilityMap = dict()
        vacMap = dict()
        
        for x in nums:
            availabilityMap[x] = availabilityMap.get(x,0) + 1
            
        for y in nums:
            if availabilityMap.get(y) <= 0: #
                continue
            elif vacMap.get(y,0) > 0:   ##Vacancy found in a sub sequence
                availabilityMap[y] = availabilityMap[y] - 1
                vacMap[y] = vacMap[y]-1
                vacMap[y+1] = vacMap.get(y+1,0) + 1
            elif availabilityMap.get(y,0) > 0 and availabilityMap.get(y+1,0) > 0 and availabilityMap.get(y+2,0) > 0:  ## starting a new subssequence
                availabilityMap[y] = availabilityMap[y]-1
                availabilityMap[y+1] = availabilityMap[y+1]-1
                availabilityMap[y+2] = availabilityMap[y+2]-1
                vacMap[y+3] = vacMap.get(y+3,0)+1
            else:
                return False
        return True

                
            
        