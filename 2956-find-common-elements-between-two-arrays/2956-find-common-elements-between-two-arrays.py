class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [0,0]
        d1 = {}
        d2 = {}
        for i in nums1:
            if i in d1:
                d1[i] += 1
            else:
                d1[i] = 1
        for i in nums2:
            if i in d2:
                d2[i] += 1
            else:
                d2[i] = 1
        for i in d1:
            if i in d2:
                ans[0] += d1[i]
        for i in d2:
            if i in d1:
                ans[1] += d2[i]     
        return ans