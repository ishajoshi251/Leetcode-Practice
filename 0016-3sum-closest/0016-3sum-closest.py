class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        diff = float("inf")
        res = 0
        for i in range(len(nums)-2):
            #skip duplicates
            
            l = i + 1
            r = len(nums) -1
        
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total == target:
                    return total

                if abs(total - target) < diff:
                    diff = abs(total - target)
                    res = total

                if total < target:
                    l += 1
                else:
                    r -= 1
                
        return res
