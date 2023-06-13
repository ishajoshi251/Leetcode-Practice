#{ 
 # Driver Code Starts


#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def removeOuter(self, S):
        # Code here
        count = 1
        temp = ""
        ans = ""
        i = 1
        while i<len(S):
            if S[i] == '(':
                count += 1
                temp += '('
            else:
                count -=1
                if count != 0:
                    temp += ')'
            if count == 0:
                ans += temp
                temp = ""
                count = 1
                i +=1
            i += 1
        return ans
                

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        s = input()
        ob = Solution()
        res = ob.removeOuter(s)
        print(res)
# } Driver Code Ends