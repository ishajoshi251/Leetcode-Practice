class Solution(object):
    
        
      
    def dfs(self, x, y, s, board, idx, found):
        if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
            return
        
        if s[idx] != board[x][y]:
            return
        
        if idx == len(s) - 1:
            found[0] = True
            return
        
        temp = board[x][y]
        board[x][y] = '*'
        
        self.dfs(x + 1, y, s, board, idx + 1, found)
        self.dfs(x - 1, y, s, board, idx + 1, found)
        self.dfs(x, y + 1, s, board, idx + 1, found)
        self.dfs(x, y - 1, s, board, idx + 1, found)
        
        board[x][y] = temp
    def exist(self, board, word):
        n = len(board)
        m = len(board[0])
        
        found = [False]
        
        for i in range(n):
            for j in range(m):
                self.dfs(i, j, word, board, 0, found)
                if found[0]:
                    return True
        
        return False
        