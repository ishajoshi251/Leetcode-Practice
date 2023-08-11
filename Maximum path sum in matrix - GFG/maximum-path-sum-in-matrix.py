#User function Template for python3

class Solution:
    def maximumPath(self, N, matrix):
        # code here
        for i in range(1,N):
            for j in range(N):
                if j == 0:
                    matrix[i][j] += max(matrix[i - 1][j], matrix[i - 1][j + 1])
                elif j == N - 1:
                    matrix[i][j] += max(matrix[i - 1][j], matrix[i - 1][j - 1])
                else:
                    matrix[i][j] += max(matrix[i - 1][j], matrix[i - 1][j - 1], matrix[i - 1][j + 1])
        maxi = float('-inf')
        for i in range(N):
            if matrix[N-1][i]>maxi:
                maxi = matrix[N-1][i]
        return maxi


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        Matrix = [[0]*N for i in range(N)]
        for itr in range(N*N):
            Matrix[(itr//N)][itr%N] = int(arr[itr])
        
        ob = Solution()
        print(ob.maximumPath(N, Matrix))

# } Driver Code Ends