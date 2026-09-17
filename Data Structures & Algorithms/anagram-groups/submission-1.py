class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Method 1: The Sorted String as the Key
        d={}
        for st in strs:
            k = "".join(sorted(st))
            # d[k]=st this saves only 1 value to the key
            if k not in d: # 
                d[k]=[]
            d[k].append(st)
        return list(d.values())
        
        
            