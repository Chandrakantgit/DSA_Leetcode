class Solution:
    def reverseWords(self, s: str) -> str:
        wordArray = s.split(" ")
        ansString = ""
        space = " "
        while len(wordArray) > 0:
            if len(wordArray) ==1:
                ansString += wordArray.pop(0)[::-1]
            else:   
                ansString += wordArray.pop(0)[::-1]
                ansString += space
            
        return ansString