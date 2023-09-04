#User function Template for python3
class Solution:
	def minCoins(self, arr, M, T):
		# code here
        n = len(arr)
        dp = [[0 for _ in range(T + 1)] for _ in range(n)]

        for i in range(T + 1):
            if i % arr[0] == 0:
                dp[0][i] = i // arr[0]
            else:
                dp[0][i] = int(1e9)

        for ind in range(1, n):
            for target in range(T + 1):
                notTake = 0 + dp[ind - 1][target]
                take = int(1e9)
                if arr[ind] <= target:
                    take = 1 + dp[ind][target - arr[ind]]
                dp[ind][target] = min(notTake, take)

        ans = dp[n-1][T]
        if ans >= int(1e9):
            return -1
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		v,m = input().split()
		v,m = int(v), int(m)
		coins = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minCoins(coins,m,v)
		print(ans)

# } Driver Code Ends