class Solution:
    def isPeak(self,mat,row,col):
        dr = [0,-1,1,0]
        dc = [1,0,0,-1]
        for i in range(4):
            nr = row+dr[i]
            nc = col+dc[i]
            if nr>=0 and nc>=0 and nr<len(mat) and nc<len(mat[0]) and mat[nr][nc]>mat[row][col]:
                return False
        return True
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        ans = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if self.isPeak(mat,i,j):
                    return [i,j]
        return [-1,-1]
                
                