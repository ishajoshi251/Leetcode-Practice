#User function Template for python3
class Solution:
	def isDivisible(self, s):
		# code here
        odd = 0
        even = 0
        for i in range(len(s)):
            if s[i] == '1':
                if i%2 == 0:
                    odd += 1
                else:
                    even += 1
        if abs(odd-even)%3:
            return 0
        else:
            return 1

#{ 
 # Driver Code Starts

#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		ob = Solution()
		ans = ob.isDivisible(s)
		print(ans)

# } Driver Code Ends