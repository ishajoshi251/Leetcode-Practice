#User function Template for python3

import sys
from typing import List
sys.setrecursionlimit(10**8)
class Solution:
    def dfs(self, r, c, grid, base_r, base_c, l, n, m):
        l.append((r - base_r, c - base_c))
        stack = [(r, c)]
        dr = [0, 0, 1, -1]
        dc = [1, -1, 0, 0]
        
        while stack:
            r, c = stack.pop()
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 1:
                    l.append((nr - base_r, nc - base_c))
                    grid[nr][nc] = 0
                    stack.append((nr, nc))
    def countDistinctIslands(self, grid : List[List[int]]) -> int:
        # code here
        n = len(grid)
        m = len(grid[0])
        s = set()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    l = []
                    self.dfs(i,j,grid,i,j,l,n,m)
                    s.add(tuple(l))
        return len(s)
                    
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n,m=map(int,input().strip().split())
        grid=[]
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        obj=Solution()
        print(obj.countDistinctIslands(grid))
# } Driver Code Ends