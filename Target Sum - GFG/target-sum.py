#User function Template for python3

class Solution:
    def findTargetSumWays(self, nums, n, d):
        # code here 
        mod = 10**9+7
        K = sum(nums)+d
        if K%2 != 0 :
            return 0
        K //= 2
        dp = [[0 for j in range(K+1)] for i in range(n+1)]
        for i in range(n+1):
            dp[i][0] = 1

        for i in range(1,n+1):
            for j in range(K+1):
                if j>=nums[i-1]:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n][K]%mod

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=list(map(int,input().split()))
        target = int(input())
        ob = Solution()
        print(ob.findTargetSumWays(arr,N, target))
# } Driver Code Ends