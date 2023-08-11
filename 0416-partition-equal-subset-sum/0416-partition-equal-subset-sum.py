class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        N = len(nums)
        K = sum(nums)
        if K%2 != 0 :
            return 0
        K //= 2
        dp = [[False for j in range(K+1)] for i in range(N+1)]
        for i in range(N+1):
            dp[i][0] = True
        for j in range(1,K+1):
            dp[0][j] = False
        for i in range(1,N+1):
            for j in range(1,K+1):
                if j>=nums[i-1]:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[N][K]