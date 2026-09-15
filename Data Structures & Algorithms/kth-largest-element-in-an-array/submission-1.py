class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hep=[]
        #temp=[]
        for i in range(len(nums)):
            hep.append(-nums[i])
        heapq.heapify(hep)
        while k>0:
            temp=heapq.heappop(hep)
            k=k-1
        return -(temp)