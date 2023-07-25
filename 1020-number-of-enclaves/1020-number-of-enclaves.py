class Solution(object):
    def dfs(self,r,c,grid):
        grid[r][c] = 0
        dr = [0,0,1,-1]
        dc = [1,-1,0,0]
        for i in range(4):
            nr = r+dr[i]
            nc = c+dc[i]
            if nr<len(grid) and nr>=0 and nc<len(grid[0]) and nc>=0 and grid[nr][nc] == 1:
                self.dfs(nr,nc,grid)
    def numEnclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])
        count = 0
        for i in range(n):
            for j in range(m):
                if (i == 0 or i == n-1 or j == 0 or j == m-1) and grid[i][j] == 1:
                    self.dfs(i,j,grid)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    count += 1
        return count