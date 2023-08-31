#User function Template for python3

class Solution:

    def longestKSubstr(self, s, k):
        # code here
        d = {}
        i = 0
        j = 0
        maxi = 0
        n = len(s)
        while j<n:
            if s[j] not in d:
                d[s[j]] = 1
            else:
                d[s[j]] += 1
            if len(d) == k:
                maxi = max(maxi,j-i+1)
            while len(d)>k:
                d[s[i]] -= 1
                if d[s[i]] == 0:
                    d.pop(s[i])
                i += 1
                
            j += 1
        if maxi == 0:
            return -1
        else:
            return maxi    
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()
        k = int(input())

        solObj = Solution()

        ans = solObj.longestKSubstr(s, k)

        print(ans)

# } Driver Code Ends