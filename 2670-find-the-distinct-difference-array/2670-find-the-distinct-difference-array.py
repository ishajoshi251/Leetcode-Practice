class Solution(object):
    def distinctDifferenceArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in range(len(nums)):
            ans.append(len(set(nums[:i+1]))-len(set(nums[i+1:])))
        return ans
        