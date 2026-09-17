from collections import defaultdict

class Solution:
    # same as solution 1 but with default dict
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=defaultdict(list)
        for st in strs:
            k = "".join(sorted(st))
            d[k].append(st)
        return list(d.values())