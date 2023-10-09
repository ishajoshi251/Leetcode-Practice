#User function Template for python3

class Solution:
    def longestPalindrome(self, s):
        # code here
        
        maxi = 1
        start = 0
        for k in range(1,len(s)):
            i = k-1
            j = k+1
            while i>=0 and j<len(s) and s[i] == s[j]:
                if j-i+1>maxi:
                    maxi = j-i+1
                    start = i
                j += 1
                i -= 1
            i = k-1
            j = k
            while i>=0 and j<len(s) and s[i] == s[j]:
                if j-i+1>maxi:
                    maxi = j-i+1
                    start = i
                j += 1
                i -= 1
        return s[start:start+maxi]
                
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        S = input().strip()
        ob=Solution()
        print(ob.longestPalindrome(S))
# } Driver Code Ends