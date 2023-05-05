class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums == sorted(nums):
            return True
        elif nums == sorted(nums,reverse=True):
            return True
        else:
            return False