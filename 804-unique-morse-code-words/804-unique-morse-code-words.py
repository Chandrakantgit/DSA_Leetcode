class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        ans = set()
        ref = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for x in words:
            temp = ""
            for y in x:
                temp = temp + ref[ord(y)-97]
            ans.add(temp)     
        return len(ans)
                
                