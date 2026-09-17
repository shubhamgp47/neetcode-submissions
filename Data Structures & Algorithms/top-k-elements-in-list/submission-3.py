from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ''' Counter producesdictionary-like object:
            keys → numbers
            values → frequencies
            and most common eturns the top k most frequent elements, sorted by frequency.'''
        temp=Counter(nums).most_common(k) 
        return [num for num, freq in temp]
