class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        if k == len(nums):
            return nums
        for i in range(len(nums)-k):
            temp = nums.pop(0)
            nums.append(temp)
        return nums
            
            
            
            
        