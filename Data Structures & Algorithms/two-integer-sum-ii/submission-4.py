class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mp=defaultdict(int)
        for i in range(len(numbers)):
            tmp=target-numbers[i]
            if mp[tmp]: # for first iteration it will always be false
                return [mp[tmp], i+1]
            mp[numbers[i]] = i+1
        return []
        