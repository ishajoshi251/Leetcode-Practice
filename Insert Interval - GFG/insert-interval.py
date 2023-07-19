#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def insertNewEvent(self, N, intervals, newEvent):
        # Code here
        res = []
        i = 0
        while i<N and intervals[i][1]<newEvent[0]:
            res.append(intervals[i])
            i += 1
        while i<N and intervals[i][0]<=newEvent[1]:
            newEvent[0] = min(intervals[i][0],newEvent[0])
            newEvent[1]= max(intervals[i][1],newEvent[1])
            
            i += 1
        res.append(newEvent)
        while i<N:
            res.append(intervals[i])
            i += 1
        return res

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        intervals = [list(map(int, input().split())) for i in range(N)]
        newEvent = list(map(int, input().split()))
        ob = Solution()
        res = ob.insertNewEvent(N, intervals, newEvent)
        print('[', end = '')
        for i in range(len(res)):
            print('[', end = '')
            print(str(res[i][0])+','+str(res[i][1]), end = '')
            print(']', end = '')
            if i < len(res)-1:
                print(',', end='')
        print(']')
# } Driver Code Ends