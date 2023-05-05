class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        flag = 0
        i = j =0
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                flag = 1
                break
            elif nums[i]>nums[i+1]:
                break
        
        if flag == 1:
            while i<len(nums)-1:
                if nums[i] <= nums[i+1]:
                    i += 1
                    
                else:
                    return False
                
        else:
            while j<len(nums)-1:
                if nums[j] >= nums[j+1]:
                    j += 1
                    
                else:
                    return False
                
        return True
            
        
            