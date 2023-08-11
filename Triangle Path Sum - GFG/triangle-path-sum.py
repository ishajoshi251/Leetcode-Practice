#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def minimizeSum(self, n, triangle):
        # Code here
        for i in range(n-2,-1,-1):
            for j in range(i+1):
                a = triangle[i][j]+triangle[i+1][j]
                b = triangle[i][j]+triangle[i+1][j+1]
                triangle[i][j] = min(a,b)
        return triangle[0][0]

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n = int(input())
        triangle = [list(map(int, input().split())) for _ in range(n)]
        ob = Solution()
        res = ob.minimizeSum(n, triangle)
        print(res)
# } Driver Code Ends