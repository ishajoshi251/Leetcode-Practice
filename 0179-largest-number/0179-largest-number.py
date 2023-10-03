class Solution:
   
    def compare(self, a, b):
        return int(a + b) > int(b + a)

    def largestNumber(self, nums):
        nums = [str(num) for num in nums]
        nums.sort(key=lambda x: x * 10, reverse=True)  # Use lambda function for comparison
        ans = ''.join(nums)
        
        if ans[0] == '0':
            return '0'
        
        return ans
