#User function Template for python3
class Solution:
    
    def check(self, temp):
        if temp[0] in ['a', 'e', 'i', 'o', 'u'] and temp[-1] not in ['a', 'e', 'i', 'o', 'u']:
            return True
        return False

    def helper(self, ind, S, temp, arr):
        if ind == len(S):
            if len(temp) > 0:
                if self.check(temp):
                    arr.append(temp)
            return

        # Include the current character in the subsequence
        self.helper(ind + 1, S, temp + S[ind], arr)

        # Skip the current character
        self.helper(ind + 1, S, temp, arr)

    def allPossibleSubsequences(self, S):
        ans = []
        self.helper(0, S, "", ans)
        
        
        ans = list(set(ans))
        ans.sort()
        return ans
        
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        S = input()
        ans=set()
        ob = Solution()
        ans = ob.allPossibleSubsequences(S)
        if(len(ans)==0):
            print(-1, end = "")
        else:
            for i in ans:
                print(i,end=" ")
        print()
# } Driver Code Ends