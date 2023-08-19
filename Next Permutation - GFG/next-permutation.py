#User function Template for python3

class Solution:
    def nextPermutation(self, N, arr):
        # code here
        ind1 = -1
        for i in range(N-2,-1,-1):
            if arr[i]<arr[i+1]:
                ind1 = i
                break
        if ind1 == -1:
            arr = arr[::-1]
            return arr
        
        for i in range(N-1,ind1,-1):
            if arr[i]>arr[ind1]:
               arr[ind1],arr[i] = arr[i],arr[ind1]
               break
        
        arr[ind1+1:] = arr[ind1+1:][::-1]
    
        return arr
        
      
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        ans = ob.nextPermutation(N, arr)
        for i in range(N):
            print(ans[i],end=" ")
        print()
# } Driver Code Ends