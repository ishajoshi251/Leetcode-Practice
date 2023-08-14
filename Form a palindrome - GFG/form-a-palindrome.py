#User function Template for python3

class Solution:
    def countMin(self, s):
        # code here
        s2 = s[::-1]
        dp = [[0 for j in range(len(s)+1)]for i in range(len(s)+1)]
        for i in range(1,len(s)+1):
            for j in range(1,len(s)+1):
                if s[i-1] == s2[j-1]:
                    dp[i][j] = 1+dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return len(s)-dp[len(s)][len(s)]
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        Str = input()
        

        solObj = Solution()

        print(solObj.countMin(Str))
# } Driver Code Ends