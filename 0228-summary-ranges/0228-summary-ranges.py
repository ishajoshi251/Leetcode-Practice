class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        
        start = 0
        end = 0
        ans = []
        i = 0
        while i<len(nums):
            start = nums[i]
            while i+1<len(nums) and nums[i]+1 == nums[i+1]:
                i += 1
            end = nums[i]
            if start == end:
                ans.append(str(start))
            else:
                ans.append(str(start)+'->'+str(end))
            
            i += 1
                
                
        return ans
                
                