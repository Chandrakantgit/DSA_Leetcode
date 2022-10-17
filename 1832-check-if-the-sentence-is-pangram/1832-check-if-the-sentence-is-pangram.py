class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        arr = []
        for x in sentence:
            arr.append(x)
        st = set(arr)
        if len(st) == 26:
            return True
        else:
            return False
            
        