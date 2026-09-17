class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # by counting each charater without sorting
        if len(s) != len(t):
            return False

        countS={}
        countT={}
        
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0) # dict.get(key, default)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        if countS == countT:
            return True
        else:
            return False