class Solution(object):
    def matrixSum(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: int
        """
        n = len(nums)
        m = len(nums[0])
        for i in range(n):
            nums[i].sort()
        summ =maxi= 0
        for i in range(m):
            for j in range(n):
                maxi = max(maxi,nums[j][i])
            summ += maxi
        
        return summ