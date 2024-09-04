class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        if len(nums) == 2 and nums[0] == nums[1]:
            return 1
        
            
        k = 1
        i = 0
        j = 1
        while j<=len(nums)-1:
            
            while nums[i] == nums[j] and j<len(nums)-1:
                j += 1          
            nums[i+1] = nums[j]
            
            i += 1  
            j += 1  
            k += 1
        if nums[k-2] == nums[k-1]:
            k -= 1
        return k
        