#User function Template for python3

class Solution:
	def MakeZeros(self, matrix):
		# Code here
        n = len(matrix)
        m = len(matrix[0])
        temp = [row[:] for row in matrix]
        
        x = [0, 0, 1, -1]
        y = [1, -1, 0, 0]
        
        for i in range(n):
            for j in range(m):
                if not temp[i][j]:
                    sum_val = 0
                    for k in range(4):
                        nrow = i + x[k]
                        ncol = j + y[k]
                        if 0 <= nrow < n and 0 <= ncol < m:
                            sum_val += temp[nrow][ncol]
                            matrix[nrow][ncol] = 0
                    matrix[i][j] = sum_val
         
        return matrix
                    
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n); m = int(m);
		matrix = []
		for _ in range(n):
			matrix.append(list(map(int,input().split())))
		ob = Solution()
		ob.MakeZeros(matrix)
		for i in range(n):
			for j in range(m):
				print(matrix[i][j], end = " ")
			print()
# } Driver Code Ends