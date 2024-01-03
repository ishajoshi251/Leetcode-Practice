class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        '''
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            if grid[i][0] == 0:
                for j in range(m):
                    if grid[i][j] == 1:
                        grid[i][j] == 0
                    else:
                        grid[i][j] == 1
        for j in range(1,m):
            zero = one = 0
            for i in range(n):
                if grid[i][j] == 1:
                    one += 1
                else:
                    zero += 1
            if zero>one:
                for i in range(n):
                    if grid[i][j] == 1:
                        grid[i][j] = 0
                    else:
                        grid[i][j] = 1
        ans = 0
        for i in range(n):
        
            count = 0
            for j in range(m-1,-1,-1):
                if grid[i][j] == 1:
                    ans += 2**count
                count += 1
        return ans
        '''
        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            if grid[i][0] == 0:
                for j in range(m):
                    grid[i][j] = 1 - grid[i][j]

        for i in range(1, m):
            count0 = sum(grid[j][i] == 0 for j in range(n))
            count1 = n - count0
            if count0 > count1:
                for j in range(n):
                    grid[j][i] = 1 - grid[j][i]

        total_sum = 0
        for i in range(n):
            count = 0
            for j in range(m - 1, -1, -1):
                if grid[i][j] == 1:
                    total_sum += 2**count
                count += 1

        return total_sum