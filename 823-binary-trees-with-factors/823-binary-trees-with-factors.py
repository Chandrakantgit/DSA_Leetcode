class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        
        arr = sorted(arr)
        FactorMap = dict()
        for i in range(0,len(arr)):
            count = 1
            for j in range(0,i):
                if arr[i]%arr[j] == 0 and arr[i]//arr[j] in FactorMap:
                    count += FactorMap.get(arr[j]) * FactorMap.get(arr[i]//arr[j])
            FactorMap[arr[i]] = count
        return (sum(FactorMap.values()))%(10**9 + 7)
                
        