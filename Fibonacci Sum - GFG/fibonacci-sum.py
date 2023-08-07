#User function Template for python3

class Solution:
    def fibSum (self,N):
        #code here
        if N==0 or N==1:
            return N
        s = 1
        prev2 = 0
        prev1 = 1
        curr = 0
        for i in range(2,N+1):   
            curr = (prev1+prev2)%1000000007
            
            prev2 = prev1
            prev1 = curr
            s += curr       
        return s%1000000007

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        ob = Solution()
        print(ob.fibSum(N))
# } Driver Code Ends