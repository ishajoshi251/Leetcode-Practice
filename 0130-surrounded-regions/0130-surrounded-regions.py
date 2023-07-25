class Solution:
    def dfs(self,r,c,board,n,m):
        board[r][c] = '#'
        dr = [0,0,1,-1]
        dc = [1,-1,0,0]
        for i in range(4):
            nr = r+dr[i]
            nc = c+dc[i]
            if nr>=0 and nr<n and nc>=0 and nc<m and board[nr][nc] == 'O':
                self.dfs(nr,nc,board,n,m)
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])
        for i in range(n):
            for j in range(m):
                if (i==0 or i == n-1 or j ==0 or j==m-1) and board[i][j] == 'O':
                    self.dfs(i,j,board,n,m)
        for i in range(n):
            for j in range(m):
                if board[i][j] == '#':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
        return board