class Solution:
    def updateMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        q = []
        n = len(grid)
        m = len(grid[0])
        ans = [[-1 for j in range(m)]for i in range(n)]
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    ans[i][j] = 0
                    q.append([i,j])
        delrow = [-1,0,1,0]
        delcol = [0,1,0,-1]
        
        while q:
            size = len(q)
            for i in range(size):
                row = q[0][0]
                col = q[0][1]
            
                q.pop(0)
                
                for i in range(4):
                    nrow = delrow[i]+row
                    ncol = delcol[i]+col
                    if nrow>=0 and nrow<n and ncol>=0 and ncol<m and ans[nrow][ncol] == -1:
                        q.append([nrow,ncol])
                        ans[nrow][ncol] = ans[row][col] +1
        return ans
                    
        
   
        