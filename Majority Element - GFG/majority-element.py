#User function template for Python 3

class Solution:
    def majorityElement(self, A, N):
        #Your code here
        ele = -1
        count = 0
        for i in range(N):
            if A[i] == ele:
                count += 1
            elif count == 0:
                ele = A[i]
                count += 1
            else:
                count -= 1
        c = N//2
        a = 0
        for i in range(N):
            if A[i] == ele:
                a += 1
                if a>c:
                   return ele
        return -1
       

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            
            obj = Solution()
            print(obj.majorityElement(A,N))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends