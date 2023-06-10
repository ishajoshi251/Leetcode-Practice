class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
         1 2 3 4 100 200
        """
        s = set(nums)
        l = 0
        maxi = 0
        for i in range(len(nums)):
            if nums[i]-1 not in s:
                curr = nums[i]
                l = 1
                while curr+1 in s:
                    curr = curr+1
                    l += 1
            maxi = max(maxi,l)
        return maxi
                