class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        n = len(s2)
        l=0

        if k>n:
            return False

        s1_dict = {}
        subDict = dict()
        for s in s1:
            if s in s1_dict:
                s1_dict[s] += 1
            else:
                s1_dict[s] = 1
        r = 0
        while r < n:
            if s2[r] in subDict:
                subDict[s2[r]] += 1
            else:
                subDict[s2[r]] = 1  

            if r-l+1 == k:
                if subDict == s1_dict:
                    return True     
                           
                subDict[s2[l]] -= 1
                if subDict[s2[l]] == 0:
                    del subDict[s2[l]]
                l += 1
            
            r += 1

        return False










        


        