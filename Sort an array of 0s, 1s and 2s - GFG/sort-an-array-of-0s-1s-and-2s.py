#User function Template for python3

class Solution:
    def sort012(self,arr,n):
        # code here
        mid = low = 0
        high = n-1
        while mid<=high:
            if arr[mid] == 0:
                arr[low],arr[mid] = arr[mid],arr[low]
                mid += 1
                low += 1
            elif arr[mid] == 1:
                mid += 1
            else:
                arr[high],arr[mid] = arr[mid],arr[high]
                high -= 1
        return arr
                

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends