#User function Template for python3
class Solution:
	def setBit(self, N):
		# code here
        X = N
        count = 0
        while N:
            if N&1 == 0:
                X = X|(1<<count)
                break
            count += 1
            N = N>>1
        return X

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())

		ob = Solution()
		ans = ob.setBit(N)
		print(ans)




# } Driver Code Ends