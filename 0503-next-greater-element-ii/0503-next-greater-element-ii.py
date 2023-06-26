class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = []
        ans = []
        for i in range(len(nums)-1,-1,-1):
            stack.append(nums[i])
        for i in range(len(nums)-1,-1,-1):
            while stack and nums[i]>=stack[-1]:
                stack.pop()
            if len(stack) == 0:
                ans.append(-1)
            else:
                ans.append(stack[-1])
            stack.append(nums[i])
        return ans[::-1]
        