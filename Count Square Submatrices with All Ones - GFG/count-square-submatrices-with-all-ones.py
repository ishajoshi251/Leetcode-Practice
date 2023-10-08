#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def countSquares(self, N, M, matrix):
       
        dp = [[0 for j in range(M)]for i in range(N)]
        s = 0
        for j in range(M):
            dp[0][j] = matrix[0][j]
            if dp[0][j] == 1:
                s+= 1
        for i in range(N):
            dp[i][0] = matrix[i][0]
            if dp[i][0] == 1:
                s+= 1
        if matrix[0][0] == 1:
            s -= 1
        for i in range(1,N):
            for j in range(1,M):
                if matrix[i][j] == 0:
                    dp[i][j] = 0
                    continue
                dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1
                s += dp[i][j]
        return s
                

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N, M = list(map(int, input().split()))
        matrix = [list(map(int, input().split())) for i in range(N)]
        ob = Solution()
        res = ob.countSquares(N, M, matrix)
        print(res)
# } Driver Code Ends