#User function Template for python3

class Solution:
	def pushZerosToEnd(self,arr, n):
    	# code here
        right = 0
        left = 0
        while right<n:
            if arr[right] == 0:
                right += 1
            else:
                arr[right],arr[left] = arr[left],arr[right]
                right += 1
                left += 1
        return arr
         
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.pushZerosToEnd(arr, n)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1
# } Driver Code Ends