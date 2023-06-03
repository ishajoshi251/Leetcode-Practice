class Solution(object):
    def countNicePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        good = 0
        for i in range(len(nums)):
            s=str(nums[i])
            rev = s[::-1]
            intt = int(rev)
            curr = (nums[i] - intt)%1000000007
            if curr in d:
                good += d[curr]
                d[curr] += 1
            else:
                d[curr] = 1
        return good%1000000007
        