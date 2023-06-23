#User function Template for python3

class Solution:
    def sieveOfEratosthenes(self, N):
    	#code here 
    	ans = []
        arr = [0]*(N+1)
        for i in range(2,N+1):
            if arr[i] == 0:
                for j in range(i*i,N+1,i):
                    arr[j] = 1
        for i in range(2,N+1):
            if arr[i] == 0:
                ans.append(i)
        return ans
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.sieveOfEratosthenes(N)
        for i in ans:
            print(i, end=" ")
        print()
# } Driver Code Ends