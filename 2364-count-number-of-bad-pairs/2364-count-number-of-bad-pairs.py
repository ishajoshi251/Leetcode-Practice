class Solution(object):
    def countBadPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        n = len(nums)
        good = 0
        for i in range(len(nums)):
            curr = nums[i] - i
            if curr in d:
                good += d[curr]
                d[curr] += 1
            else:
                d[curr] = 1
            
           
        total = (n*(n-1))//2
        return total-good