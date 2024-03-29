class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        r, c, cnt = 0, n - 1, 0
        while r < m and c >= 0:
            if grid[r][c] < 0:
                cnt += m - r
                c -= 1
            else:
                r += 1
        return cnt
        