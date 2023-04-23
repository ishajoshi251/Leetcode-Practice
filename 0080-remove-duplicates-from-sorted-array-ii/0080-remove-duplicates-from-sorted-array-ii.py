class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ind = 2
        for i in range(2,len(nums)):
            if nums[ind-2] != nums[i]:
                nums[ind] = nums[i]
                ind += 1
        return ind