#User function Template for python3

class Solution:
    def lenOfLongSubarr (self, arr, n, k) : 
        #Complete the function
        curr  = 0
        maxi  = 0
        d = {}
        for i in range(n):
            curr += arr[i]
            if curr == k:
                maxi = max(maxi,i+1)
            if curr-k in d:
                maxi = max(maxi,i-d[curr-k])
            if curr not in d:
                d[curr] = i
        return maxi
               




#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    n, k = map(int , input().split())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    print(ob.lenOfLongSubarr(arr, n, k))




# } Driver Code Ends