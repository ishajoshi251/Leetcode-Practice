class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
         
        intervals.sort()
        start = intervals[0][0]
        end = intervals[0][1]
        ans = []
        for i in range(1,len(intervals)):
            if intervals[i][0]<=end:
                end = max(end,intervals[i][1])
                
            else:
                ans.append([start,end])
                start = intervals[i][0]
                end = intervals[i][1]
        ans.append([start,end])
        return ans
    
    #1 2 8  15 18 21 26
    #3 6 10 18 20 25 30
     # i    j