class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                x = nums[i]|nums[j]
                if (x&1) == 0:
                    return True
        return False