#User function Template for python3

class Solution:
    def maxDepth(self, s):
        # Code here
        new = ""
        for i in s:
            if i == '(' or i == ')':
                new += i
        count = 0
        maxi = 0
        for i in new:
            if i =='(':
                count += 1
            else:
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