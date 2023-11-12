class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        maxi = float('-inf')
        n = len(nums)
        for i in range(n):
            for j in range(n):
                if abs(nums[i]-nums[j])<=min(nums[i],nums[j]):
                    maxi = max(maxi,nums[i]^nums[j])
        return maxi