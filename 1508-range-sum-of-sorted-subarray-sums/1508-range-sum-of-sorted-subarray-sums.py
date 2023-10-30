class Solution:
    
    def solve(self,nums):
        subarrays = []
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n + 1):
                subarray = nums[i:j]
                subarrays.append(sum(subarray))

        return subarrays
        
    
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        mod = 1000000007
        ans = self.solve(nums)
        ans.sort()
        a = sum(ans[left-1:right])
        return a%mod
        