#User function Template for python3

class Solution:
    def canReach(self, A, N):
        # code here 
        goal = N-1
        for i in range(N-1,-1,-1):
            if A[i]+i >= goal:
                goal = i
        if goal == 0:
            return 1
        else:
            return 0

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        A=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.canReach(A,N))
# } Driver Code Ends