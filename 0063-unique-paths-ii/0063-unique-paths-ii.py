class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return 0
        dp = [[0 for j in range(m)]for i in range(n)]
        flag = False
        for i in range(m):
            if grid[0][i] == 1 or flag:
                dp[0][i] = 0
                flag = True
            else:
                dp[0][i] = 1
        flag = False
        for i in range(n):
            if grid[i][0] == 1 or flag:
                dp[i][0] = 0
                flag = True
            else:
                dp[i][0] = 1
        for i in range(1,n):
            for j in range(1,m):
                if grid[i][j] == 1:
                    continue
                else:
                    dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[-1][-1]