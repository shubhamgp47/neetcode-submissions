class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # same as 1
        intervals.sort(key = lambda p:p[0])
        output=[intervals[0]]
        for start,end in intervals:
            if output[-1][1]>=start:
                output[-1][1]=max(output[-1][1],end)
            else:
                output.append([start,end])
        return output