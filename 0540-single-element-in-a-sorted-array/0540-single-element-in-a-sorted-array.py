class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums)== 1:
            return nums[0]
        if nums[0]!=nums[1]:
            return nums[0]
        if nums[-1]!=nums[-2]:
            return nums[-1]
        low = 1
        high = len(nums)-2
        while low<=high:
            mid = low+(high-low)//2
            if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
                return nums[mid]
            if (mid%2 != 0 and nums[mid-1]==nums[mid] )or(mid%2 == 0 and nums[mid]==nums[mid+1]):
                low = mid+1
            else:
                high = mid-1
        return -1