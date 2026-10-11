class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        maxSize = 0
        string_set = set()
        size = 0
        for r in range(len(s)):
            while s[r] in string_set:
                string_set.discard(s[l])
                l += 1
                size -= 1
                
            
            string_set.add(s[r])
            size += 1
            maxSize = max(size, maxSize)
        
        return maxSize
        


            

                
        




        