#User function Template for python3
import math
class Solution:
    def sumcount(self, nums, mid):
        sum_ = 0
        for num in nums:
            sum_ += num // mid + (num % mid != 0)
        return sum_

    def smallestDivisor(self, nums, k):
        s = 1
        e = max(nums)
        ans = 0

        while s <= e:
            mid = s + (e - s) // 2
            if self.sumcount(nums, mid) <= k:
                ans = mid
                e = mid - 1
            else:
                s = mid + 1

        return ans







        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n, K = list(map(int, input().split()))
        nums = list(map(int, input().split()))
        ob = Solution()
        res = ob.smallestDivisor(nums, K)
        print(res)
# } Driver Code Ends