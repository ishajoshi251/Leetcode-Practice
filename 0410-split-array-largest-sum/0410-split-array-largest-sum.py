class Solution:
    def isPossible(self,nums,k,mid):
        curr = 0
        sub = 1
        for i in nums:
            curr += i
            if curr>mid:
                sub += 1
                curr = i
        if sub>k:
            return False
        return True
    
    def splitArray(self, nums: List[int], k: int) -> int:
        low = max(nums)
        high = sum(nums)
        res = high
        while low<=high:
            mid = low+(high-low)//2
            if self.isPossible(nums,k,mid):
                res = mid
                high = mid-1
            else:
                low = mid+1
        return res