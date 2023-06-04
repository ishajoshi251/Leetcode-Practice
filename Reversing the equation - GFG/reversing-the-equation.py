#User function Template for python3

class Solution:
    def reverseEqn(self, s):
        # code her
        stack = []
        a = ""
        for i in s:
            
            if i in ['+','-', '*', '/']:
                stack.append(a)
                stack.append(i)
                a = ""
            else:
                a += i
        if len(a)>0:
            stack.append(a)
        b = ""
        while stack:
            b += stack.pop()
        return b
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.reverseEqn(s)
        print(ans)
# } Driver Code Ends