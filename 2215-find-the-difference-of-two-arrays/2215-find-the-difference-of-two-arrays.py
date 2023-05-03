class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans = []
        a = []
        b = []
        for i in nums1:
            if i in nums2:
                continue
            else:
                if i not in a:
                    a.append(i)
                else:
                    continue
        ans.append(a)
        for j in nums2:
            if j in nums1:
                continue
            else:
                if j not in b:
                    b.append(j)
                else:
                    continue
        ans.append(b)
        return ans
                