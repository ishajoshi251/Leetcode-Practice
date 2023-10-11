#User function Template for python3

class Solution:
    def matrixMultiplication(self, n, arr):
        # code here
        dp=[[0]*n for i in range(n)]
        #we start filling diagonally where (i-j)>=2
        for l in range(2,n):
            #as we move ahead both r,c +1
            c=l
            for r in range(0,n-l):
                dp[r][c]=float('inf')
                #k is 1 here r=0,c=4, in (0,1)(1,4)
                for k in range(r+1,c):
                    dp[r][c]=min(dp[r][c],dp[r][k]+dp[k][c]+arr[r]*arr[k]*arr[c])
                c+=1
        return dp[0][n-1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        print(ob.matrixMultiplication(N, arr))
# } Driver Code Ends