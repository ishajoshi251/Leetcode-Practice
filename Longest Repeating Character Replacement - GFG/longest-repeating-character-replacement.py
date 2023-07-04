#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def characterReplacement(self, s, k):
        # Code here
        res = 0 
        left = 0
        d = {}
        for right in range(len(s)):
            if s[right] in d:
                d[s[right]] += 1
            else:
                d[s[right]] = 1
           
            while (right-left+1)- max(d.values()) > k:
                d[s[left]] -= 1
                left += 1
                
            res = max(right-left+1,res)
        return res

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range(t):
        S = input().strip()
        K = int(input())
        ob = Solution()
        res = ob.characterReplacement(S, K)
        print(res)
# } Driver Code Ends