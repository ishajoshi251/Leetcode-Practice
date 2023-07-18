#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def minRemoval(self, N, intervals):
        # Code here
        res = []
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
        
#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        intervals = [list(map(int, input().split())) for i in range(N)]
        ob = Solution()
        res = ob.minRemoval(N, intervals)
        print(res)
# } Driver Code Ends