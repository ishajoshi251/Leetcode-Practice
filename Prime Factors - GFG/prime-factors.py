#User function Template for python3

class Solution:
	def AllPrimeFactors(self, n):
		# Code here
		'''
        ans = []
        s = set()
        for i in range(2,N+1):
            while N%i == 0:
                s.add(i)
                N = N//i
        for i in s:
            ans.append(i)
        a = ans.sort()
        return a
        '''
        ans = set()
        v = []
        for i in range(2, n+1):
            while n % i == 0:
                ans.add(i)
                n = n // i
        for it in ans:
            v.append(it)
        return sorted(v)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		ob = Solution()
		ans = ob.AllPrimeFactors(N)
		for _ in ans:
			print(_, end = " ")
		print()
# } Driver Code Ends