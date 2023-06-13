#User function Template for python3

class Solution:
    def maxOdd(self, s):
        for i in range(len(s)-1,-1,-1):
            if int(s[i])%2 != 0:
                s = s[:i+1]
                return s
        return ""
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        ob = Solution()
        print(ob.maxOdd(s))
# } Driver Code Ends