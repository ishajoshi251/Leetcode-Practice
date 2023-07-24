class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        vis = [[1 for j in range(m)]for i in range(n)]
        q = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append([i,j,0])
                    vis[i][j] = 2
        maxi = 0
        dr = [0,0,-1,1]
        dc = [1,-1,0,0]
        
        while q:
            r = q[0][0]
            c= q[0][1]
            t = q[0][2]
            q.pop(0)
            maxi = max(maxi,t)
            for i in range(4):
                nr = r + dr[i]
                nc = c+dc[i]
                if nr>=0 and nc>=0 and nr<n and nc<m and grid[nr][nc] == 1 and vis[nr][nc] != 2:
                    vis[nr][nc] =2
                    q.append([nr,nc,t+1])
                    
            
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and vis[i][j] != 2:
                    return -1
        return maxi
            
                
            