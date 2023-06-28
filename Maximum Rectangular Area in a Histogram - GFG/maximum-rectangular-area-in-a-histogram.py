#User function Template for python3


class Solution:
    
    #Function to find largest rectangular area possible in a given histogram.
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
                
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

# by Jinay Shah 

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.getMaxArea(a))
# } Driver Code Ends