class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        d = {}
        sum = 0
        count = 0
        for i in range(len(nums)):
            sum += nums[i]
            if sum == goal:
                count += 1
            if sum-goal in d:
                count += d[sum-goal]
            if sum in d:
                d[sum] += 1
            else:
                d[sum] = 1
        return count