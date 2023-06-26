#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def nextGreaterElement(self, N, arr):
        # Code here
        stack = []
        ans = []
        for i in range(N-1,-1,-1):
            stack.append(arr[i])
        # 5 4 3 2 1
        for i in range(N-1,-1,-1):
            while stack and stack[-1]<=arr[i]:
                stack.pop()
            if len(stack)==0:
                ans.append(-1)
            else:
                ans.append(stack[-1])
            stack.append(arr[i])
            
        return ans[::-1]

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.nextGreaterElement(N, arr)
        for val in res:
            print(val, end = ' ')
        print()
# } Driver Code Ends