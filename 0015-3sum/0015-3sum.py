class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()  
        n = len(nums)
        for i in range(n-2):
            j = i+1
            k = n-1
            while j<k:
                s = nums[i]+nums[j]+nums[k]
                if s == 0:
                    ans.append([nums[i],nums[j],nums[k]])
                   
                    j += 1
                    k -= 1
                elif s>0:
                    k -= 1
                else:
                    j += 1
        new = []
        for i in ans:
            if i not in new:
                new.append(i)
        return new