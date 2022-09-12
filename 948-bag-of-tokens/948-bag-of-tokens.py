class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens = sorted(tokens)
        maxScore = 0
        score = 0
        l = 0
        r = len(tokens)-1

        while l <= r : 
            if tokens[l] <= power:
                score+=1
                power -= tokens[l]
                l+=1
                maxScore = max(maxScore,score)
            elif score > 0:
                power += tokens[r]
                r-=1
                score-=1    
            else:
                break
        return maxScore
        