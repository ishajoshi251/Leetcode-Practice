class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        maxi = 0
        n = len(grid)
        m = len(grid[0])
        for i in range(n-2):
            for j in range(m-2):
                curr = 0
                curr += grid[i][j]+grid[i][j+1]+grid[i][j+2]+grid[i+1][j+1]+grid[i+2][j]+grid[i+2][j+1]+grid[i+2][j+2]      
                maxi = max(maxi,curr)
        return maxi