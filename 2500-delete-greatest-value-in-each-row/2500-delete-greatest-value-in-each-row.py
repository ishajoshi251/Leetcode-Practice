class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        ans = 0
        for i in range(n):
            grid[i].sort()
        for j in range(m):
            maxi = -11111
            for i in range(n):
                maxi = max(maxi,grid[i][j])
            ans += maxi
        return ans