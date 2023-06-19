#User function Template for python3

class Solution:
	def NthRoot(self, n, m):
		# Code here
        low =1
        high =m
        while low<=high:
            mid = (high+low)//2
            if mid**n == m:
                return mid
            elif mid**n<m:
                low = mid+1
            else:
                high = mid-1
        return -1
                

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n); m = int(m);
		ob = Solution()
		ans = ob.NthRoot(n, m)
		print(ans)
# } Driver Code Ends