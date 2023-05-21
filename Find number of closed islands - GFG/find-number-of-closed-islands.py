#User function Template for python3

class Solution:
	
    def dfs(self,i, j, matrix):
        if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]) or matrix[i][j] == 0:
            return
        matrix[i][j] = 0
        self.dfs(i+1, j, matrix)
        self.dfs(i-1, j, matrix)
        self.dfs(i, j+1, matrix)
        self.dfs(i, j-1, matrix)


    def closedIslands(self,matrix, N, M):
        for i in range(N):
            for j in range(M):
                if (i == 0 or j == 0 or i == N-1 or j == M-1) and matrix[i][j] == 1:
                    self.dfs(i, j, matrix)
    
        count = 0
        for i in range(N):
            for j in range(M):
                if matrix[i][j] == 1:
                    count += 1
                    self.dfs(i, j, matrix)
    
        return count   

#{ 
 # Driver Code Starts
#Initial Template for Python 3
		
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N, M = map(int,input().split())
        matrix = []
        for i in range(N):
            nums = list(map(int,input().split()))
            matrix.append(nums)
        obj = Solution()
        print(obj.closedIslands(matrix, N, M))
# } Driver Code Ends