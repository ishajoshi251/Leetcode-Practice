#User function Template for python3

class Solution:
    def Search(self, n, arr, k):
        # code here
        low = 0
        high = n-1
        while low<=high:
            mid = low+(high-low)//2
            if arr[mid] == k:
                return 1
            if arr[mid] == arr[low] and arr[mid] == arr[high]:
                low = low+1
                high = high-1
                continue
            if arr[low]<=arr[mid]:
                if arr[low]<=k and k<=arr[mid]:
                    high = mid-1
                else:
                    low = mid+1
            else:
                if arr[mid]<=k and k<=arr[high]:
                    low = mid+1
                else:
                    high = mid-1
        return 0
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        k = int(input())
        ob = Solution()
        ans = ob.Search(n, arr, k)
        print(ans)
        tc -= 1
# } Driver Code Ends