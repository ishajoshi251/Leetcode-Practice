#User function Template for python3

class Solution:
    def maximumProfit(self, p, n, f):
        #Code here
        s=0
        b=-p[0]
        for i in range(1,n):
            s=max(s,b+p[i]-f)
            b=max(b,s-p[i])
        return s

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n=int(input())
        prices = list(map(int, input().split()))
        fee=int(input())
        ob = Solution()
        print(ob.maximumProfit(prices, n, fee))
# } Driver Code Ends