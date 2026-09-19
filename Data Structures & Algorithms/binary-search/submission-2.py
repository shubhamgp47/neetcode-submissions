class Solution:
    def search(self, nums: List[int], target: int) -> int:
        'best'
        l,r=0,len(nums)-1

        def bs(l,r):
            if l > r:
                return -1
            mid= l+(r-l)//2
            if nums[mid]==target:
                return mid
            elif nums[mid] < target:
                l=mid+1
                return bs(l,r)
            else: # nums[mid] > target:
                r=mid-1
                return bs(l,r)
        
        return bs(l,r)