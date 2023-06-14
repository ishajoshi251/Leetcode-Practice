class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        ans = []
        ans = sorted(nums,key=lambda x:(d[x],-x))
        return ans
    