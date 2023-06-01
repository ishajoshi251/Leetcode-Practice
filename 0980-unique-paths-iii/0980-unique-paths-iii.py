class Solution(object):
       
        
        def __init__(self):
            self.result = 0

        def dfs(self, i, j, grid, count, empty):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == -1 or grid[i][j] == -2:
                return

            if grid[i][j] == 2 and count - 1 == empty:
                self.result += 1
                return

            temp = grid[i][j]
            grid[i][j] = -2

            self.dfs(i + 1, j, grid, count + 1, empty)
            self.dfs(i - 1, j, grid, count + 1, empty)
            self.dfs(i, j + 1, grid, count + 1, empty)
            self.dfs(i, j - 1, grid, count + 1, empty)

            grid[i][j] = temp
        def uniquePathsIII(self, grid):
            n = len(grid)
            m = len(grid[0])
            count = 0
            start = 0
            end = 0
            zero_count = 0

            for i in range(n):
                for j in range(m):
                    if grid[i][j] == 1:
                        start = i
                        end = j
                    elif grid[i][j] == 0:
                        zero_count += 1

            self.dfs(start, end, grid, count, zero_count)
            return self.result
        