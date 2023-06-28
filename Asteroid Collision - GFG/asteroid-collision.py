#User function Template for python3

class Solution:
    def asteroidCollision(self, n, ast):
        # Code here
      
        ans = []
        stack = []
        for i in range(n):
            if ast[i]>0:
                stack.append(ast[i])
            else:
                
                while stack and stack[-1]< -1*ast[i]:
                    stack.pop()
                    
                if stack and stack[-1] == -1*ast[i]:
                    stack.pop()
                    continue
                if len(stack) == 0:
                    ans.append(ast[i])
                
        while stack:
            ans.append(stack[0])
            stack.pop(0)
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        asteroids = list(map(int, input().split()))
        ob = Solution()
        res = ob.asteroidCollision(N, asteroids)
        for val in res:
            print(val, end = ' ')
        print()
# } Driver Code Ends