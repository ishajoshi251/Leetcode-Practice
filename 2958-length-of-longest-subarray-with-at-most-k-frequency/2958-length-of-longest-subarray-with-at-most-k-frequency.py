class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        maxi = 0
        j = 0
        i = 0
        d = {}
        while j<len(nums):
            if nums[j] in d:
                d[nums[j]] += 1
            else:
                d[nums[j]] = 1
            if d[nums[j]]>k:
                while d[nums[j]]>k:
                    d[nums[i]] -= 1
                    i += 1
            maxi = max(maxi,j-i+1)
            j += 1
        return maxi