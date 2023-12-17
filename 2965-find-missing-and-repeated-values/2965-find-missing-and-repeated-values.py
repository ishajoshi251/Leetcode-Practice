class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        ans = []
        d = {}
        mis=rep=0
        n = len(grid)*len(grid)
        for i in range(1,n+1):
            d[i] = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if d[grid[i][j]] == 0:
                    d[grid[i][j]] = 1
                elif d[grid[i][j]] == 1:
                    d[grid[i][j]] += 1
                else:
                    continue
        for key in d.keys():
            if d[key] == 2:
                rep = key
            if d[key] == 0:
                mis = key
        ans.append(rep)
        ans.append(mis)
        return ans