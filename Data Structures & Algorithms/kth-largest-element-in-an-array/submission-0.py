class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        sorted_nums=sorted(nums)
        #nums.sort() # in place sort
        return sorted_nums[-k]
