class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[0] * (i + 1) for i in range(n)]
        for i in range(n):
            dp[-1][i] = triangle[-1][i]
        for i in range(n-2,-1,-1):
            for j in range(i+1):
                a = triangle[i][j]+dp[i+1][j]
                b = triangle[i][j]+dp[i+1][j+1]
                dp[i][j] = min(a,b)
        return dp[0][0]