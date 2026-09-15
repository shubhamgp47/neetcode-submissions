class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_substring=set() # all unique characters currently inside the window
        l=0
        res=0 # longest window seen so far
        for r in range(len(s)):
            while s[r] in unique_substring: # if r is duplicate
                unique_substring.remove(s[l]) # remove previous occurance
                l=l+1 # increase left index
            unique_substring.add(s[r]) # add to substring
            res = max(res,r-l+1) # calculate max
        return res

