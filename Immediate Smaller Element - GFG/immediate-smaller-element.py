#User function Template for python3
class Solution:

	def immediateSmaller(self,arr,n):
		# code here
        ans = []
        stack = []
        stack.append(arr[0])
        for i in range(1,n):
            if stack[-1]>arr[i]:
                ans.append(arr[i])
                stack.pop()
            else:
                ans.append(-1)
            stack.append(arr[i])
        ans.append(-1)
        arr[:] = ans[:]
        return arr

#{ 
 # Driver Code Starts
if __name__ == '__main__':
    tcs=int(input())

    for _ in range(tcs):
        n=int(input())
        arr=[int(x) for x in input().split()]
        ob = Solution()
        ob.immediateSmaller(arr,n)
        for x in arr:
            print(x, end=" ")
        print()
# } Driver Code Ends