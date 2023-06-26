class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d= {}
        for i in range(len(nums2)):
            d[nums2[i]] = i
        ans = []
        for i in range(len(nums1)):
            ind = d[nums1[i]]
            flag = 0
            for j in range(ind+1,len(nums2)):
                if nums2[j]>nums1[i]:
                    ans.append(nums2[j])
                    flag = 1
                    break
            
            if flag == 0:
                ans.append(-1)
        
        return ans