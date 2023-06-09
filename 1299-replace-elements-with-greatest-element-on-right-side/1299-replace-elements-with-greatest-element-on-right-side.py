class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        ans = []
        ans.append(-1)
        maxi = arr[-1]
        for i in range(len(arr)-1,0,-1):
            if arr[i]>maxi:
                maxi = arr[i]
            ans.append(maxi)
        return ans[::-1]