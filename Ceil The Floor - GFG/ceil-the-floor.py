#User function Template for python3




def getFloorAndCeil(A, N, X):
    # code here
    ceil = -1
    floor = -1
    A.sort()
    low= 0
    high = N-1
    while low<=high:
        mid = low+(high-low)//2
        if A[mid] == X:
            floor = A[mid]
            ceil = A[mid]
            return (floor,ceil)
        elif A[mid]<X:
            low = mid+1
        else:
            high = mid-1
    if low != 0:
        floor = A[low-1]
    if low != N:
        ceil = A[low]
    return (floor,ceil)
    #5 5 5 6 6 6 8 9 

#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))

        ans = getFloorAndCeil(arr, n, x)
        print(str(ans[0]) + " " + str(ans[1]))
        tc -= 1

# } Driver Code Ends