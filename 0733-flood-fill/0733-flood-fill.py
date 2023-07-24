class Solution:
    def dfs(self,sr,sc,grid,image,color,old,drow,dcol):
        grid[sr][sc] = color
        n = len(image)
        m = len(image[0])
        for i in range(4):
            nr = sr+drow[i]
            nc = sc+dcol[i]
            if m>nc and nc>=0 and n>nr and nr>=0 and image[nr][nc] == old and grid[nr][nc] != color:
                self.dfs(nr,nc,grid,image,color,old,drow,dcol)
                
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        grid = image
        drow=[1,0,0,-1]
        dcol=[0,-1,1,0]
        old = image[sr][sc]
        self.dfs(sr,sc,grid,image,color,old,drow,dcol)
        return grid