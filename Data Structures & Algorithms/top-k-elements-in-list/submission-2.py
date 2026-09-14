from collections import Counter
from typing import List
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap=[]
        for num, feq in count.items(): # has to be items
            heapq.heappush(heap, [feq, num])
            if len(heap) > k:
                heapq.heappop(heap)

        return [num for feq, num in heap]
