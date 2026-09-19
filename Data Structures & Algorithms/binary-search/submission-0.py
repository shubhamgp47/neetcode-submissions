class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # naive
        for n in nums:
            if n==target:
                return nums.index(n)
        return -1