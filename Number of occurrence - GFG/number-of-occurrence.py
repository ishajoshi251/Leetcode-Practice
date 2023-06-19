#User function Template for python3
class Solution:
    def findFirst(self,arr,n,x):
        ind = -1
        start = 0
        end = n-1
        while start<=end:
            mid = start+(end-start)//2
            if arr[mid] == x:
                ind = mid
                
            if arr[mid] >= x:
                end = mid-1
            elif arr[mid]<x:
                start = mid+1
        return ind
    def findLast(self,arr,n,x):
        ind = -1
        start = 0
        end = n-1
        while start<=end:
            mid = start+(end-start)//2
            if arr[mid] == x:
                ind = mid
                
            if arr[mid] <=x:
                start = mid+1
            elif arr[mid]>x:
                end = mid-1
        return ind
    
	def count(self,arr, n, x):
		# code here
		ind1 = -1
		ind2 = -1
		ind1 = self.findFirst(arr,n,x)
		ind2 = self.findLast(arr,n,x)
		if ind1 == -1 and ind2 == -1:
		    return 0
		    
		return ind2-ind1+1
#{ 
 # Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.count(arr, n, x)
        print(ans)
        tc -= 1

# } Driver Code Ends