class Solution:
    def findFirst(self,nums,target):
            start = 0
            end = len(nums)-1
            idx = -1
            while start<=end:
                mid = start+(end-start)//2
                if nums[mid] >= target:
                    end = mid-1
                    
                elif nums[mid] < target:
                    start = mid+1
                if nums[mid] == target:
                    idx = mid
                
            return idx
        
    def findLast(self,nums,target):
            start = 0
            end = len(nums)-1
            idx = -1
            while start<=end:
                mid = start+(end-start)//2
                if nums[mid] <= target:
                    start =mid+ 1
                    
                elif nums[mid] > target:
                    end = mid-1
                    
                if nums[mid] == target:
                    idx = mid
                
            return idx
        
        
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1]*2
        
        
        res[0] = self.findFirst(nums,target)
        res[1] = self.findLast(nums,target)
        return res
    