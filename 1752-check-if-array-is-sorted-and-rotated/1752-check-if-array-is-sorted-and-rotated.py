class Solution(object):
    def check(self, nums):
        """
        [6,10,6]
        [7,9,1,1,1,2,3]
        :type nums: List[int]
        :rtype: bool
        """
        count = 0
        if nums[0]<nums[-1]:
            count += 1
        for i in range(1,len(nums)):
            if nums[i-1]>nums[i]:
                count += 1
            else:
                continue
        if count <= 1:
            return True
        return False