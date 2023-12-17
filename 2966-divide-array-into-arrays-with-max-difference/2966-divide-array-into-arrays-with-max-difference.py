class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        temp = []
        ans = []
        for i in range(len(nums)):
            temp.append(nums[i])
            if len(temp) == 3:
                if temp[1]-temp[0]>k:
                    return []
                if temp[2]-temp[0]>k:
                    return []
                if temp[2]-temp[1]>k:
                    return []
            if len(temp) == 3:
                ans.append(temp)
                temp = []
            
                
        return ans
                