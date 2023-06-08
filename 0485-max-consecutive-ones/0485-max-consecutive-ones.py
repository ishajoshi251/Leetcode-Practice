class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxi = 0
        sum = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                sum += 1
                maxi = max(sum,maxi)
            else:
                
                sum = 0
        
        return maxi
        