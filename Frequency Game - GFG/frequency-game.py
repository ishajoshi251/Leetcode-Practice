#User function Template for python3


def LargButMinFreq(arr,n):
    #code here
    d= {}
    maxi = min(arr)
    for i in arr:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    mini = min(d.values())
    
    for i in d:
        if d[i] == mini:
            maxi = max(maxi,i)
    return maxi
#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
#Iterating over test cases
for _ in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()]
    print(LargButMinFreq(arr, n))
# } Driver Code Ends