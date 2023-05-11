
class Solution:
    def countDistinct(self, A, N, K):
        # Code here
        ans = []
        d = {}
        i = 0
        j = 0
        while j<N:
            if A[j] in d:
                d[A[j]] += 1
            else:
                d[A[j]] = 1
            if j-i+1 == K:
                ans.append(len(d))
                d[A[i]] -= 1
                if d[A[i]] == 0:
                    d.pop(A[i])
                i += 1
                j += 1
                
            elif j-i+1<K:
                j += 1
                
                
        return ans

#{ 
 # Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n,k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        res = Solution().countDistinct(arr, n, k)
        for i in res:
            print (i, end = " ")
        print ()
# } Driver Code Ends