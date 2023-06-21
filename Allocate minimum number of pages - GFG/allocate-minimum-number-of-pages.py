class Solution:
    def isPossible(self,A,N,M,mid):
        allocated_s = 1
        pages = 0
        for i in range(N):
            if A[i]>mid:
                return False
            if pages+A[i]>mid:
                allocated_s += 1
                pages = 0
                pages += A[i]
            else:
                pages += A[i]
        if allocated_s > M:
            return False
        
        return True
    #Function to find minimum number of pages.
    def findPages(self,A, N, M):
        #code here
        if M>N:
            return -1
        ans = -1
        low = A[0]
        high = sum(A)
        while low<=high:
            mid = (low+high)//2
            if self.isPossible(A,N,M,mid):
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans
                

'''
[12,34,67,90] n = 4 student = 2

conditions: 
book to one student
minimum 1 book
contiguous

12 | 34 67 90   maxi = 191
12 34 | 67 90    157
12 34 67 |90     113

low                  mid                high
12                   107                203
1->12+34
2->67
3->90

108                  155                203
1->12+34+67
2->90

ans = 155

108                   131                154
ans = 131

108                   119               130
ans = 119

108                   113               118
ans = 113
'''



#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        n=int(input())
        
        arr=[int(x) for x in input().strip().split()]
        m=int(input())
        
        ob=Solution()
        
        print(ob.findPages(arr,n,m))
# } Driver Code Ends