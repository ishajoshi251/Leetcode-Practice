#User function Template for python3

class Solution:
    def sumOfNaturals(self, n):
        # code here 
        mod = 10**9+7
        s = (n*(n+1))//2
        return s%mod

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        
        ob = Solution()
        print(ob.sumOfNaturals(n))
# } Driver Code Ends