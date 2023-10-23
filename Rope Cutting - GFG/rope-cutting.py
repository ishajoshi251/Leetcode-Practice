#User function Template for python3

class Solution:
    def RopeCutting (self, arr, n) : 
        #Complete the function
        #1 2 2 5 5 6 6 8 9 11
        #9 7 5 3 2 1
        arr.sort()
        last_idx = 0
        ans = []
        i = 0
        while i<n:
            while i+1<n and arr[i] == arr[i+1]:
                i += 1
            last_idx = i
            if last_idx == n-1:
                break
            ans.append(n-last_idx-1)
            i += 1
            
        return ans
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

  
for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    ob=Solution()
    res = ob.RopeCutting(arr, n)
    print(*res)






# } Driver Code Ends