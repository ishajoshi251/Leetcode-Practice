#User function template for Python

class Solution:	
	def remove_duplicate(self, arr, N):
		# code here
        i = 1
        while i<len(arr):
            if arr[i] == arr[i-1]:
                arr.pop(i)
            else:
                i += 1
        return len(arr)
#{ 
 # Driver Code Starts
#Initial template for Python

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        N = int(input())
        A = list(map(int, input().strip().split()))
        ob = Solution()
        n = ob.remove_duplicate(A,N)
        for i in range(n):
            print(A[i], end=" ")
        print()


# } Driver Code Ends