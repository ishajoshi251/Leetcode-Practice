class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        d = {}
        dom = maxi = 0
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
            if d[i]>maxi:
                maxi = d[i]
                dom = i
        count = 0
        for i in range(len(nums)):
            if nums[i] == dom:
                count += 1
            if count*2 > i+1:
                if (d[dom]-count)*2 > len(nums)-i-1:
                    return i
        return -1