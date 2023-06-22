#User function Template for python3


def KthMissingElement (arr,  n, k) : 
    #Complete the function
    for i in range(n-1):
        if arr[i]+1 == arr[i+1]:
            continue
        else:
            while arr[i]+1 != arr[i+1]:
                k -= 1
                if k == 0:
                    return arr[i]+1
                arr[i] += 1
    return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

for _ in range(0,int(input())):
    
    n, K = map(int ,input().split())
    arr = list(map(int,input().strip().split()))
    res = KthMissingElement(arr, n, K)
    print(res)



# } Driver Code Ends