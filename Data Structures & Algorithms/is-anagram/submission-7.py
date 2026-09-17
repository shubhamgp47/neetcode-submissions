class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''defaultdict is just a normal dictionary with one superpower - If we access a missing key, it automatically creates it with a default value.
        count = defaultdict(int) means every missing key should start at 0'''
        if len(s) != len(t):
            return False
        
        countS=defaultdict(int)
        countT=defaultdict(int)

        for i in range(len(s)):
            countS[s[i]] += 1
            countT[t[i]] += 1
        return countS == countT