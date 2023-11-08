class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        count = maxi = ans = 0
        n = len(grid)
        for i in range(n):
            count = 0
            for j in range(n):
                if grid[i][j] == 1:
                    count += 1
            if count>maxi:
                maxi = count
                ans = i
        return ans