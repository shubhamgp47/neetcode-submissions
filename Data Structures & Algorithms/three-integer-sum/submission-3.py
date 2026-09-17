class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result=set()
        nums.sort()
        for i in range(len(nums)):
            a=nums[i]
            if a>0: # check if first number if >0 after sorting
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue # checks if numbers are same, if so skip them
            l,r=i+1,len(nums)-1
            while l<r:
                if a + nums[l] + nums[r]==0:
                    result.add((a,nums[l],nums[r]))
                    l=l+1
                    r=r-1
                elif a + nums[l]+nums[r]<0:
                    l=l+1
                else:
                    r=r-1
        return list(result)             
