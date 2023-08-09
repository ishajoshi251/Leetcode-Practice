#User function Template for python3

class Solution:
    def maximumPoints(self, points, n):
        # Code here
        dp = [[0 for j in range(3)]for i in range(n)]
        for i in range(3):
            dp[0][i] = points[0][i]
        for i in range(1,n):
            dp[i][0] = max(dp[i-1][1],dp[i-1][2])+points[i][0]
            dp[i][1] = max(dp[i-1][0],dp[i-1][2])+points[i][1]
            dp[i][2] = max(dp[i-1][1],dp[i-1][0])+points[i][2]
        maxi = 0
        for i in range(3):
            if dp[n-1][i]>maxi:
                maxi = dp[n-1][i]
        return maxi

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        points = [list(map(int, input().split())) for _ in range(n)]
        ob = Solution()
        print(ob.maximumPoints(points, n))
# } Driver Code Ends