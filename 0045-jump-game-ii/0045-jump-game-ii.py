class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        maxi = 0
        current = 0
        for i in range(len(nums)-1):
            maxi = max(maxi,i+nums[i])
            if current == i:
                current = maxi
                jumps += 1
        return jumps