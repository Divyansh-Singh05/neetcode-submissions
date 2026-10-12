class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        freq_map = {}
        max_freq = 0
        max_len = 0
        for r,item in enumerate(s):  
            if item in freq_map:
                freq_map[item] += 1
            else :
                freq_map[item] = 1
                   
            max_freq = max(max_freq,freq_map[item])

            while (r-l+1) - max_freq > k:
                freq_map[s[l]] -= 1
                l += 1
            
            max_len = max(max_len,r-l+1)
        return max_len




        