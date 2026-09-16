class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda p:p[0]) # sort the intervals by the first value
        output = [intervals[0]] # initialize the output with first interval

        for start,end in intervals:
            if output[-1][1]>=start:
                output[-1][1]=max(output[-1][1], end)
            else:
                output.append([start,end])
        return output


