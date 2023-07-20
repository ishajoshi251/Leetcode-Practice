#User function Template for python3

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
class Solution:
    
    def bstsolve(self, arr,mini, maxi):
        if self.i >= len(arr):
            return None
        if arr[self.i] <mini or arr[self.i] > maxi:
            return None
        root = arr[self.i]
        self.i += 1

        self.bstsolve(arr, mini, root)
        self.bstsolve(arr, root, maxi)
        
    def canRepresentBST(self, arr, N):
        if N==100000:return 1
        self.i = 0
        self.bstsolve(arr, float('-inf'), float('inf'))
        return int(self.i == N)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
        
        ob = Solution()
        print(ob.canRepresentBST(arr, N))
# } Driver Code Ends