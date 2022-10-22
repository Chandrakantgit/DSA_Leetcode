from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        # [1] obtain letter frequencies
        freq = Counter(t)
        
        # [2] in this solution, we use a two-pointer sliding window 
        #    approach while keeping track of a number of unique 
        #    characters from 't' that are missing on each iteration 
        miss  = len(set(t))
        l, r  = 0, 0
        wl, wr = -1, len(s)
        
        while True:
            # [3] move right pointer while we're still 
            #    missing any of the characters from 't' 
            if r < len(s) and miss > 0:
                freq[s[r]] -= 1
                if freq[s[r]] == 0: miss -= 1
                r += 1
                
            # [4] move left pointer while we're still
            #    having a surplus of characters from 't' 
            elif l < len(s) and miss <= 0:
                # [5] the update of minimal substring happens only when
                #    we move the left pointer, i.e., when we already 
                #    have no characters from 't' missing 
                if r-l < wr-wl: wr, wl = r, l
                    
                if freq[s[l]] == 0: miss += 1
                freq[s[l]] += 1
                l += 1
                
            else:
                break
        
        return s[wl:wr] if wl >= 0 else ""