class Solution:
    def distributeTicket(self, N : int, K : int) -> int:
        # Code Here
        start = 0
        end = N + 1
    
        while start < end:
            for i in range(K):
                start += 1
                N -= 1
                if N == 0:
                    return start
    
            for i in range(K):
                end -= 1
                N -= 1
                if N == 0:
                    return end
    
        return -1






           
   
#{ 
 # Driver Code Starts
t = int(input())
for _ in range(t):
    
    N, K = map(int, input().split())
    
    obj = Solution()
    res = obj.distributeTicket(N, K)
    
    print(res)
# } Driver Code Ends