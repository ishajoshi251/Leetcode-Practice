#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def maxChildren(self, N, M, greed, sz):
        # Code here
        greed.sort()
        sz.sort()
        i = 0
        j = 0
        count = 0
        while i<N and j<M:
            if greed[i]<=sz[j]:
                count += 1
                i+= 1
            j += 1
        return count

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N, M = list(map(int, input().split()))
        greed = list(map(int, input().split()))
        sz = list(map(int, input().split()))
        ob = Solution()
        res = ob.maxChildren(N, M, greed, sz)
        print(res)
# } Driver Code Ends