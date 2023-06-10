#User function Template for python3

class Solution:
    def findSubArraySum(self, Arr, N, k):
        # code here
        d = {}
        count = 0
        d[0] = 1
        s = 0
        for i in range(N):
            s += Arr[i]
            if s-k in d:
                count += d[s-k]
            if s in d:
                d[s] += 1
            else:
                d[s] = 1
        return count

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        Arr = input().split()
        for itr in range(N):
            Arr[itr] = int(Arr[itr])
        k = int(input())
        ob = Solution()
        print(ob.findSubArraySum(Arr, N, k))
# } Driver Code Ends