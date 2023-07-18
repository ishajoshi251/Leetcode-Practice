#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def minCandy(self, N, ratings):
        # Code here
        count = [1]*N
        if N == 1:
            return 1
        if N == 2:
            if ratings[0]!=ratings[1]:
                return sum(count)+1
            else:
                return sum(count)
        
                
        for i in range(1,N):
            if ratings[i-1] < ratings[i]:
                count[i] = count[i-1]+1
                
        count2=[1]*N
        for i in range(N-2,-1,-1):
            if ratings[i+1]<ratings[i]:
                count2[i] = count2[i+1]+1
                
        
    
        s = 0
        for i in range(N):
            s += max(count[i],count2[i])
            
                
                
            
        return s

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        ratings = list(map(int, input().split()))
        ob = Solution()
        res = ob.minCandy(N, ratings)
        print(res)
# } Driver Code Ends