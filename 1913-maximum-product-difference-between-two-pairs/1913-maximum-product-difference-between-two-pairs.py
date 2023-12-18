class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        a = nums[0]
        b = nums[1]
        c = nums[-2]
        d = nums[-1]
        diff = (c*d)-(a*b)
        return diff