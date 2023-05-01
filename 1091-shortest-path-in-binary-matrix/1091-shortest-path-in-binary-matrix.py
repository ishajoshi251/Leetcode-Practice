class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        '''if grid[0][0] != 0 or grid[-1][-1] != 0: 
            return -1

        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1), (1, -1), (-1, -1), (-1, 1), (1, 1)]
        q = deque()
        distance = [[float('inf')] * (COLS) for _ in range(ROWS)]

        distance[0][0] = 1 # starting cost is 1
        q.append((0, 0, distance[0][0])) #currRow, currCol, currDistance      
        
        while q:
            currRow, currCol, currDistance = q.popleft()
            for dr, dc in directions:
                r = currRow + dr
                c = currCol + dc
                if r in range(ROWS) and c in range(COLS) and grid[r][c] == 0:
                    if distance[r][c] > currDistance + 1: 
                        distance[r][c] = currDistance + 1 #update distance if smaller found
                        q.append((r, c, distance[r][c]))
        if distance[-1][-1] == float('inf'): #path not possible
            return -1
        return distance[-1][-1]'''
        if grid[0][0] != 0 or grid[-1][-1] != 0 :
            return -1
        row = len(grid)
        col = len(grid[0])
        direction = [(-1,0),(0,1),(1,0),(0,-1),(1,-1),(-1,-1),(-1,1),(1,1)]
        q = []
        dist  = [[float('inf') for j in range(col)]for i in range(row)]
        dist[0][0] = 1
        q.append([0,0,dist[0][0]])
        while q:
            currrow = q[0][0]
            currcol = q[0][1]
            currdis = q[0][2]
            q.pop(0)
            for dr,dc in direction:
                nrow = currrow + dr
                ncol = currcol + dc
                if nrow>= 0 and nrow<row and ncol>=0 and ncol<col and grid[nrow][ncol] == 0:
                    if dist[nrow][ncol]>currdis+1:
                        dist[nrow][ncol]=currdis+1
                        q.append([nrow,ncol,dist[nrow][ncol]])
        if dist[-1][-1] == float('inf'):
            return -1
        return dist[-1][-1]
        