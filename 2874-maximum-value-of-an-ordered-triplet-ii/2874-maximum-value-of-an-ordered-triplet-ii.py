class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        result = 0
        max_diff = max_num =0
        for i in nums:
            result = max(result,max_diff*i)
            max_diff = max(max_diff,max_num-i)
            max_num = max(max_num,i)
        return result