#{ 
 # Driver Code Starts
#Initial Template for Python 3



# } Driver Code Ends
#User function Template for python3

class Solution:
    def maxScore(self, cardPoints, N, k):
        # Code here
        ans = maxi = 0
        for i in range(k):
            ans += cardPoints[i]
        maxi = ans
        j = N-1
        for i in range(k-1,-1,-1):
            ans -= cardPoints[i]
            ans += cardPoints[j]
            j -= 1
            
            maxi = max(maxi,ans)
        return maxi

#{ 
 # Driver Code Starts.


if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N, k = map(int, input().split())
        cardPoints = list(map(int, input().split()))
        ob = Solution()
        res = ob.maxScore(cardPoints, N, k)
        print(res)
# } Driver Code Ends