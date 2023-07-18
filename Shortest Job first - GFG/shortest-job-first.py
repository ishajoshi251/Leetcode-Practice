#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def solve(self, bt):
        # Code here
        bt.sort()
        completion_time = []
        s = 0
        for i in range(len(bt)):
            s+=bt[i]
            completion_time.append(s)
        avg = []
        for i in range(len(bt)):
            avg.append(completion_time[i]-bt[i])
        ans = sum(avg)//len(avg)
        return ans
        

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n = int(input())
        bt = list(map(int, input().split()))
        ob = Solution()
        res = ob.solve(bt)
        print(res)
# } Driver Code Ends