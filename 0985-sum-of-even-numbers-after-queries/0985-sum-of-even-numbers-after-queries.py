class Solution(object):
    def sumEvenAfterQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        s = 0
        for i in nums:
            if i%2 == 0:
                s += i
        for i in range(len(queries)):
            ind = queries[i][1]
            val = queries[i][0]
            prev = nums[ind]
            change = nums[ind] + val
            if prev%2 == 0:
                s -= prev
            if change%2 == 0:
                s += change
            nums[ind] = change
            ans.append(s)
        return ans
            
        