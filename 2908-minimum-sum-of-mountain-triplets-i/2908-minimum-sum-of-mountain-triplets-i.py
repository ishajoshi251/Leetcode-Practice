class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        mini = 1000000000
        s = 0
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                for k in range(j+1,len(nums)):
                    if nums[i]<nums[j] and nums[k]<nums[j]:
                        s = nums[i]+nums[j]+nums[k]
                        mini = min(s,mini)
        if mini == 1000000000:
            return -1
        return mini