#User function Template for python3
class Solution:

	def print2largest(self,arr, n):
		# code here
		'''
	    maxi = 0
	    smaxi = -1
	    for i in range(n):
	        if arr[i]>maxi:
	            maxi=arr[i]
	    for i in range(n):
	        if arr[i]<maxi and arr[i]>smaxi:
	            smaxi = arr[i]
	    return smaxi
	    '''
	    maxi = -1
	    smaxi = -1
	    for i in range(n):
	        if arr[i]>maxi:
	            smaxi = maxi
	            maxi=arr[i]
	        elif arr[i]>smaxi and arr[i]<maxi:
	            smaxi = arr[i]
	    return smaxi

#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.print2largest(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends