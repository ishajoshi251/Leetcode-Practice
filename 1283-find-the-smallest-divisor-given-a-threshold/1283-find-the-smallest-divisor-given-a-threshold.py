class Solution:
    def getSum(self,nums,mid):
        s = 0
        for i in range(len(nums)):
            s += ceil(nums[i]/mid)
        return s
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low = 1
        high = 1000000
        while low<=high:
            mid = low+(high-low)//2
            if self.getSum(nums,mid)>threshold:
                low = mid+1
            else:
                high = mid-1
        return low
                