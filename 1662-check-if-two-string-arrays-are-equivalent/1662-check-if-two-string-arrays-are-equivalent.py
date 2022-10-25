class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        st1 = ""
        for x in word1:
            st1 +=x
        
        st2 = ""
        for y in word2:
            st2 +=y
        
        if st1 == st2:
            return True
        else:
            return False
            
            
            
        