class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1 or nums[0] < nums[-1]:
            return nums[0]

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if mid > 0 and nums[mid - 1] > nums[mid]:  # The nums[mid] is the minimum number
                return nums[mid]
            if nums[mid] > nums[right]:  # search on the right side, because smaller elements are in the right side
                left = mid + 1
            else:
                right = mid - 1  # search the minimum in the left side
