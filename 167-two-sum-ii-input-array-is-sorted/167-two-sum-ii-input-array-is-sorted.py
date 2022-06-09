class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        val1=0
        val2=len(numbers)-1
        while val1<val2:
            if numbers[val1]+numbers[val2]==target:
                return [val1+1,val2+1]
            if numbers[val1]+numbers[val2]<target:
                val1+=1
            else:
                val2-=1