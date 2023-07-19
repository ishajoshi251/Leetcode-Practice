class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = []
        N = len(intervals)
        intervals.sort()
        start = intervals[0][0]
        end = intervals[0][1]
        for i in range(1,N):
            if end>intervals[i][0]:
                end = min(end,intervals[i][1])
            else:
                res.append([start,end])
                start = intervals[i][0]
                end = intervals[i][1]
        res.append([start,end])
        return len(intervals)-len(res)