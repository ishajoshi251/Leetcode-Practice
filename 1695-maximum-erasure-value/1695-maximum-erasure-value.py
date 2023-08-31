class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        d = {}
        i = j = maxi = s = 0
        n = len(nums)
        while j<len(nums):
            s += nums[j]
            if nums[j] not in d:
                d[nums[j]] = 1
                
            else:
                d[nums[j]] += 1
            while d[nums[j]]>1:
                d[nums[i]] -= 1
                s -= nums[i]
                
                if d[nums[i]] == 0:
                    d.pop(nums[i])
                i += 1
            maxi = max(maxi,s)
            j += 1
            
        return maxi