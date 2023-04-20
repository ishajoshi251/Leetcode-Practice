class Solution(object):
    def findUnsortedSubarray(self, arr):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(arr) == 1:
            return 0
        
        i = 0
        j = len(arr)-1
        start = 0
        end = 0
        b = 0
        a= 0
        
        while i<len(arr)-1:
            if arr[i+1]<arr[i]:
                start = i
                break
            i += 1
        while j>0:
            if arr[j-1]>arr[j]:
	            end = j
	            break
            j -= 1
        if start == 0 and end == 0:
            return 0
        mini = min(arr[start:end+1])
	   
        maxi = max(arr[start:end+1])
        for i in range(len(arr)):
            if arr[i]>mini:
                a = i
                break
        for i in range(len(arr)-1,-1,-1):
            if arr[i]<maxi:
	            b = i
	            break
        return b-a+1
        