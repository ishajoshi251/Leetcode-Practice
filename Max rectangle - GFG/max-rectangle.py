#User function Template for python3


class Solution:
    def getMaxArea(self,histogram):
        #code here
        n = len(histogram)
        left = [0]*n
        right = [0]*n
        stack = []
        for i in range(n):
            while stack and histogram[i]<=histogram[stack[-1]]:
                stack.pop()
            if not stack:
                left[i] = 0
            else:
                left[i] = stack[-1]+1
            stack.append(i)
            
        while stack:
            stack.pop()
        for i in range(n-1,-1,-1):
            while stack and histogram[i]<=histogram[stack[-1]]:
                stack.pop()
            if not stack:
                right[i] = n-1
            else:
                right[i] = stack[-1]-1
            stack.append(i)
        ans = 0
        maxi = ans
        for i in range(n):
            ans = (right[i]-left[i]+1)*histogram[i]
            maxi = max(maxi,ans)
        return maxi
                
        
    def maxArea(self,matrix, n, m):
        # code here
        ans = 0
        heights = [0]*m
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 1:
                    heights[j] += 1
                else:
                    heights[j] = 0
            ans = max(ans,self.getMaxArea(heights))
        return ans
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3



# Driver Code 
if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        R,C = map(int, input().strip().split())
        A = []
        for i in range(R):
            line = [int(x) for x in input().strip().split()]
            A.append(line)
        print(Solution().maxArea(A, R, C)) 
	
# This code is contributed 
# by SHUBHAMSINGH10 

# } Driver Code Ends