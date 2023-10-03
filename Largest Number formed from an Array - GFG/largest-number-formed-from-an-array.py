#User function Template for python3
class Solution:

	def printLargest(self,nums):
	    # code here
	    nums = [str(num) for num in nums]
        nums.sort(key=lambda x: x * 10, reverse=True)  # Use lambda function for comparison
        ans = ''.join(nums)
        
        if ans[0] == '0':
            return '0'
        
        return ans
    def compare(self, a, b):
        return int(a + b) > int(b + a)

       

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import functools

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(str, input().strip().split()))
        ob = Solution()
        ans = ob.printLargest(arr)
        print(ans)
        tc -= 1

# } Driver Code Ends