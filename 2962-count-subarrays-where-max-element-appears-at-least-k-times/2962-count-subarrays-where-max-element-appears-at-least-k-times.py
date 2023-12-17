class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        i = j = count = ans = 0
        maxi = max(nums)
        while j<len(nums):
            if nums[j] == maxi:
                count += 1
            if count>=k:
                ans += len(nums)-j
            while count>=k:
                if nums[i] == maxi:
                    count -= 1
                if count >= k:
                    ans += len(nums)-j
                i += 1
            j += 1
        return ans