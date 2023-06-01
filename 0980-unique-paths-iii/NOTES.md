'''
if r>len(grid) or c>len(grid[0]) or r<=0 or c<=0 or grid[r][c] == -1 or grid[r][c] == -2:
return
if grid[r][c] == 2 and count-1 == zero:
res += 1
return
grid[r][c] = -2
self.dfs(r+1,c,grid,count+1,zero)
self.dfs(r-1,c,grid,count+1,zero)
self.dfs(r,c+1,grid,count+1,zero)
self.dfs(r,c-1,grid,count+1,zero)
grid[r][c] = 0
return res
def uniquePathsIII(self, grid):
"""
:type grid: List[List[int]]
:rtype: int
"""
start = end  = 0
zero = 0
for i in range(len(grid)):
for j in range(len(grid[0])):
if grid[i][j] == 1:
start = i
end = j
elif grid[i][j] == 0:
zero += 1
return self.dfs(start,end,grid,0,zero,0)