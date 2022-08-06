import math

class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        test = minutesToTest/minutesToDie
        i = 0
        while math.pow(test+1,i)<buckets:
            i+=1
        return i
            
        
        
        
        
        
