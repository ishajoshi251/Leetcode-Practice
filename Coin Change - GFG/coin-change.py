#User function Template for python3

class Solution:
    def count(self, arr, n, T):
        # code here 
        dp = [[0 for j in range(T + 1)] for i in range(n)]
    
        # Initializing base condition
        for i in range(T + 1):
            if i % arr[0] == 0:
                dp[0][i] = 1
            # Else condition is automatically fulfilled,
            # as dp array is initialized to zero
        
        for ind in range(1, n):
            for target in range(T + 1):
                notTaken = dp[ind - 1][target]
                
                taken = 0
                if arr[ind] <= target:
                    taken = dp[ind][target - arr[ind]]
                    
                dp[ind][target] = notTaken + taken
        
        return dp[n - 1][T]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        sum,N = list(map(int, input().strip().split()))
        coins = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.count(coins,N,sum))

# } Driver Code Ends