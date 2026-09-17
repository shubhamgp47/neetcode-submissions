class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 2 pass
        indices = {}

        for i,j in enumerate(nums):
            indices[j]=i

        for i,j in enumerate(nums):
            complement = target - j
            if complement in indices and indices[complement] != i:
                return [i, indices[complement]]
