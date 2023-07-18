class Solution:
    def jump(self, nums: List[int]) -> int:
        max_reach = 0
        curr = 0
        jump = 0
        for i in range(len(nums)-1):
            max_reach = max(max_reach,nums[i]+i)
            if curr == i:
                curr = max_reach
                jump += 1
        return jump