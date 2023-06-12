#User function Template for python3
class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr, n):
		# code here
		pre = 1
		suff = 1
		maxi = -111111111
		flag = 0
		for i in range(n):
		    pre *= arr[i]
		    maxi = max(maxi,pre)
		    if arr[i] == 0:
		        pre = 1
		for i in range(n-1,-1,-1):
		     suff*=arr[i]
		     maxi = max(maxi,suff)
		     if arr[i] == 0:
		        suff = 1
		return maxi
		    
		        

#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends