#User function Template for python3
class Solution:
    def findKRotation(self,arr,  n):
        # code here
        low = 0
        high = n-1
        ind = 0
        mini =1000000
        while low<=high:
            mid = low+(high-low)//2
            if arr[mid]>=arr[low]:
                if mini>arr[low]:
                    mini = arr[low]
                    ind = low
                low = mid+1
            else:
                if mini>arr[mid]:
                    mini = arr[mid]
                    ind = mid
                high = mid-1
        return ind
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

	tc=int(input())
	while tc > 0:
		n=int(input())
		a=list(map(int , input().strip().split()))
		ob = Solution()
		ans=ob.findKRotation(a, n)
		print(ans)
		tc=tc-1



# } Driver Code Ends