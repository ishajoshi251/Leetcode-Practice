class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans = []
        for i in range(0,len(nums)-1,2):
            x = nums[i]
            y = nums[i+1]
            ans.append(y)
            ans.append(x)
            
        return ans