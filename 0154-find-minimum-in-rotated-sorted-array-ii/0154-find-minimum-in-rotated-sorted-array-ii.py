class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        mini = 10000
        low = 0
        high = len(nums)-1
        while low<=high:
            mid = low+(high-low)//2
            if nums[mid] == nums[low] and nums[high] == nums[mid]:
                mini = min(mini,nums[low])
                low = low+1
                high = high-1
                continue
            if nums[low]<=nums[mid]:
                mini = min(mini,nums[low])
                low = mid+1
            else:
                mini = min(mini,nums[mid])
                high = mid-1
        return mini