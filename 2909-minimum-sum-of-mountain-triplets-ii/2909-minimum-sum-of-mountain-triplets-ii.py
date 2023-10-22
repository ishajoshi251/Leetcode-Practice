
class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return -1  # Not enough elements in the list to form a valid sum.

        mini = float('inf')
        
        left = [0] * len(nums)
        left[0] = nums[0]
        right = [0] * len(nums)
        right[-1] = nums[-1]

        # Calculate the minimum elements from the left and right.
        for i in range(1, len(nums)):
            left[i] = min(left[i-1], nums[i])
        for i in range(len(nums) - 2, -1, -1):
            right[i] = min(right[i+1], nums[i])

        for j in range(1, n - 1):
            if left[j - 1] < nums[j] and nums[j] > right[j + 1]:
                # Calculate the sum of elements from left, right, and the current element.
                s = nums[j] + right[j + 1] + left[j - 1]
                mini = min(s, mini)

        if mini == float('inf'):
            return -1  # If no valid sum was found, return -1.

        return mini


            