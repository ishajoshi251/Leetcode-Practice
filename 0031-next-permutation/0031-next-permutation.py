class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        ind1 = -1
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]:
                ind1 = i
                break
        
        
        if ind1 == -1:
            nums[:] = nums[::-1]
            return nums
            
        for i in range(len(nums)-1,ind1,-1):
            if nums[i]>nums[ind1]:
                nums[ind1],nums[i] = nums[i],nums[ind1]
                break
        nums[ind1+1:] = nums[ind1+1:][::-1]
        return nums