class Solution:
    def isGood(self, nums: List[int]) -> bool:
        maxi = max(nums)
        if len(nums) != maxi+1:
            return False
        nums.sort()
        if nums[len(nums)-1] != maxi:
            return False
        i = len(nums)-2
        while maxi:
            if nums[i] != maxi:
                return False
            maxi -= 1
            i -= 1
        return True
            