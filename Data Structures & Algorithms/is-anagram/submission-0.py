class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        see=dict()
        tee=dict()
        for c in s:
            try:
                see[c] = see[c]+1
            except:
                see[c]=1
        for c in t:
            try:
                tee[c] = tee[c]+1
            except:
                tee[c]=1
        return see==tee

        