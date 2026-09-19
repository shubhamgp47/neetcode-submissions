class Solution:
    def isPalindrome(self, s: str) -> bool:
        # reversed(s) returns a iterator object, correct way -
        '''reversed_string = "".join(reversed(s)) 
        if s==reversed_string:
            return True
        return False'''
        # either keep both string or both list
        #or use slicing approach
        #cleaned = [c.lower() for c in s if c.isalnum()]
        cleaned = "".join(c.lower() for c in s if c.isalnum())
        cleaned_reversed="".join(reversed(cleaned))
        if cleaned==cleaned_reversed:
        #if cleaned==cleaned[::-1]:
            return True
        return False
