#User function Template for python3
class Solution:
    def minimumNumberOfSwaps(self,s):
        # code here 
        o, c = 0, 0
        cnt  = 0
        for i in range(len(s)):
            if s[i] == ']':
                c += 1
            else:
                if c > o:
                    #print(o,c)
                    cnt += (c-o)
                o += 1        

        return cnt
#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S=str(input())
        ob = Solution()
        print(ob.minimumNumberOfSwaps(S))
# } Driver Code Ends