class Solution:
    '''
    def dfs(self,r,c,n,m,board,ind,flag,word):
        
        if r>=n or c>=m or r<0 or c<0:
            return
        if ind == len(word)-1:
            flag = True
            
        
        if board[r][c] != word[ind]:
            return
        
        h = board[r][c]
        board[r][c] = "*"
        self.dfs(r+1,c,n,m,board,ind+1,flag,word)
        self.dfs(r,c-1,n,m,board,ind+1,flag,word)
        self.dfs(r,c+1,n,m,board,ind+1,flag,word)
        self.dfs(r+1,c,n,m,board,ind+1,flag,word)
        
        board[r][c] = h
            
        
                
                
	def isWordExist(self, board, word):
		#Code here
		ind = 0
		n = len(board)
		m = len(board[0])
		flag = False
		for i in range(n):
		    for j in range(m):
		        self.dfs(i,j,n,m,board,ind,flag,word)
		        if flag:
		            return True
		return False
	'''
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
    def isWordExist(self, board, word):
        n = len(board)
        m = len(board[0])
        
        found = [False]
        
        for i in range(n):
            for j in range(m):
                self.dfs(i, j, word, board, 0, found)
                if found[0]:
                    return True
        
        return False


#{ 
 # Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for tt in range(T):
		n, m = map(int, input().split())
		board = []
		for i in range(n):
			a = list(input().strip().split())
			b = []
			for j in range(m):
				b.append(a[j][0])
			board.append(b)
		word = input().strip()
		obj = Solution()
		ans = obj.isWordExist(board, word)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends