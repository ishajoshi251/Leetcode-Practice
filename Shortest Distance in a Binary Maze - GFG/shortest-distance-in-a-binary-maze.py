#User function Template for python3

from typing import List

class Solution:
    
    def shortestPath(self, grid: List[List[int]], source: List[int], destination: List[int]) -> int:
        # code here
        dist = [[float('inf') for j in range(len(grid[0]))]for i in range(len(grid))]
        q = []
        dr = [0,0,1,-1]
        dc = [1,-1,0,0]
        r = source[0]
        c = source[1]
        dist[r][c] = 0
        r1 = destination[0]
        c1 = destination[1]
        if source == destination:
            return 0
        if grid[r][c] == 0:
            return -1
        q.append([r,c,dist[r][c]])
        while q:
            r,c,d = q.pop(0)
            for i in range(4):
                nr = r+dr[i]
                nc = c+dc[i]
                if nr>=0 and nr<len(grid) and nc>=0 and nc<len(grid[0]) and grid[nr][nc] != 0:
                    if d+1<dist[nr][nc]:
                        dist[nr][nc] = d+1
                        q.append([nr,nc,dist[nr][nc]])
        if dist[r1][c1] == float('inf'):
            return -1
        return dist[r1][c1]
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

         
if __name__=="__main__":
    for _ in range(int(input())):
        n,m=map(int,input().strip().split())
        grid=[]
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        source = [0] * 2
        source[0], source[1] = map(int,input().strip().split())
        destination = [0] * 2
        destination[0], destination[1] = map(int,input().strip().split())
        obj=Solution()
        print(obj.shortestPath(grid, source, destination))
# } Driver Code Ends