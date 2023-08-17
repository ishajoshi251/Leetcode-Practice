
class Solution:
    def removeAdj(self,v,n):
        # Your code goes here
        stack = []
        for i in range(n):
            if not stack or stack[-1] != v[i]:
                stack.append(v[i])
            else:
                stack.pop()
        return len(stack)
    


#{ 
 # Driver Code Starts

if __name__=='__main__':
    tcs=int(input())

    for _ in range(tcs):
        n=int(input())
        v=[x for x in input().split()]
        ob = Solution()
        print(ob.removeAdj(v,n))
# } Driver Code Ends