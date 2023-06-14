#User function Template for python3

class Solution:
    def maxDepth(self, s):
        # Code here
       
        count = 0
        maxi = 0
        for i in s:
            if i =='(':
                count += 1
            elif i == ')':
                count -= 1
            maxi = max(count,maxi)
        return maxi
            
                

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        ob = Solution()
        print(ob.maxDepth(s))
# } Driver Code Ends