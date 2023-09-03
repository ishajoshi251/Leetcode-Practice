#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def help(self,temp,n,ans):
        if n == len(temp):
            ans.append(temp)
            return
        temp += '0'
        self.help(temp,n,ans)
        temp = temp[:-1]
       
        if len(temp) == 0 or temp[-1] == '0':
            temp += '1'
            self.help(temp,n,ans)
        
    def generateBinaryStrings(self, n):
        # Code here
        ans = []
        self.help("",n,ans)
        return ans

#{ 
 # Driver Code Starts.
from sys import stdout
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        ob = Solution()
        res = ob.generateBinaryStrings(N)
        for binaryString in res:
            print(binaryString, end = ' ')
        print()
# } Driver Code Ends