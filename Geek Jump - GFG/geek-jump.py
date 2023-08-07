#User function Template for python3

class Solution:
    def minimumEnergy(self, cost, n):
        # Code here
        dp = [-1]*n
        dp[0] = 0
        a=0
        b = float('inf')
        for i in range(1,n):
            a = dp[i-1]+abs(cost[i]-cost[i-1])
            if i>1:
                b = dp[i-2]+abs(cost[i]-cost[i-2])
            dp[i] = min(a,b)
        return dp[n-1]
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        height = list(map(int, input().split()))
        ob = Solution()
        print(ob.minimumEnergy(height, n))
# } Driver Code Ends