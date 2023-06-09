#User function Template for python3

def longestSubarry( A, N):
    l = 0
    maxi = 0
    i = j = 0
    while j<N:
        if A[j]>=0:
            
            l += 1
        else:
            maxi = max(maxi,l)
            l = 0
            
        j += 1 
    maxi = max(maxi,l)
    return maxi
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        print(longestSubarry(a, n))

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends