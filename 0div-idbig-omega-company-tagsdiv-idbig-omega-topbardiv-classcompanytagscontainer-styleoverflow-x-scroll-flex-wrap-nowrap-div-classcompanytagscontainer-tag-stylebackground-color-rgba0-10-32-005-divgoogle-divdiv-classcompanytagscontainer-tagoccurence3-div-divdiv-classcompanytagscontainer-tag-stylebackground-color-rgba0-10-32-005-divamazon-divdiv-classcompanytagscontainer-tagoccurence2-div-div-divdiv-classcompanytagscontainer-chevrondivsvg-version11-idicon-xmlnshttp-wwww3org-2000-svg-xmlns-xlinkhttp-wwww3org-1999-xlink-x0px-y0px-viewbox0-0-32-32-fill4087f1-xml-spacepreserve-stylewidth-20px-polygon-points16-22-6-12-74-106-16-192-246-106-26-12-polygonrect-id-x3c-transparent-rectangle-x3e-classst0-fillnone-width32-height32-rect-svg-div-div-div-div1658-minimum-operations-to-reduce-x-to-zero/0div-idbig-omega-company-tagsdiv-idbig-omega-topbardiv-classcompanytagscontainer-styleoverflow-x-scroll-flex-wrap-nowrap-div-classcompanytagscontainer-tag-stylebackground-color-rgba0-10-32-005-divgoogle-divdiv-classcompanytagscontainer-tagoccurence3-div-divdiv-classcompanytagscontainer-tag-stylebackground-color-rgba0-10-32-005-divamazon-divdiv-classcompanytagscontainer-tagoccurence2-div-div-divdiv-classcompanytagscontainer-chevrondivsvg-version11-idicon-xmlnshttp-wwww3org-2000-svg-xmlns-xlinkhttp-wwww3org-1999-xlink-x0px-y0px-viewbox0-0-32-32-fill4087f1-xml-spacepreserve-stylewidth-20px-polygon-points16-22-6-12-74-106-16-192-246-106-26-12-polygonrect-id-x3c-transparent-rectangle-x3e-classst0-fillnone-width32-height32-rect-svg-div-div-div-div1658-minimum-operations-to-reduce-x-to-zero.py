class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total = sum(nums)
        i = 0
        j = 0
        target = total-x
        if target == 0:
            return len(nums)
        curr = 0
        ans = 0
        while j<len(nums):
            curr += nums[j]
            while i<=j and curr>target:
                curr -= nums[i]
                i += 1
            if curr == target:
                ans = max(ans,j-i+1)
           
            
            j += 1
        if ans == 0:
            return -1
        return len(nums)-ans