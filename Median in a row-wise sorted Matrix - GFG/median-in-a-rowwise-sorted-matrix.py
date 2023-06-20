#User function Template for python3

class Solution:
    '''
    def upperBound(self,row,mid):
        l = 0
        h = len(row)-1
        while l<=h:
            m = (l+h)//2
            if row[m]<=mid:
                low  = m+1
            else:
                high = m-1
            
        return l
    def median(self, matrix, R, C):
    	#code here 
        low =1
        high = 2000
        while low<=high:
            mid = (low+high)//2
            count = 0
            for i in range(len(matrix)):
                count += self.upperBound(matrix[i],mid)
            if count<=(len(matrix)*len(matrix[0]))//2:
                low = mid+1
            else:
                high = mid-1
        return low
        '''
    def countSmallerThanMid(self, row, mid):
        l = 0
        h = len(row) - 1
        while l <= h:
            md = (l + h) // 2
            if row[md] <= mid:
                l = md + 1
            else:
                h = md - 1
        return l
    def median(self, matrix, R, C):
        low = 1
        high = 1e9
        while low <= high:
            mid = (low + high) // 2
            cnt = 0
            for i in range(R):
                cnt += self.countSmallerThanMid(matrix[i], mid)
            if cnt <= (R * C) // 2:
                low = mid + 1
            else:
                high = mid - 1
        return int(low)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        r,c = map(int,input().strip().split())
        matrix = [[0 for j in range(c)] for i in range(r)]
        for i in range(r):
            t=[int(el) for el in input().split()]
            for j in range(c):
                matrix[i][j]=t[j]
        ans = ob.median(matrix, r, c);
        print(ans)
# } Driver Code Ends