class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        if grid[0][0] == 1 or grid[n-1][m-1] == 1:
            return 0
            
        path = [[0]*m for _ in range(n)]
        path[0][0] = 1
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    continue
                if r-1 >= 0:
                    path[r][c] += path[r-1][c]
                if c-1 >= 0:
                    path[r][c] += path[r][c-1]
        return path[n-1][m-1]