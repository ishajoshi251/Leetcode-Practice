class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        maxi =1
        n = len(arr)
        if arr[0]!=1:
            arr[0] = 1
            
        for i in range(1,n):
            if abs(arr[i]-arr[i-1]<=1):
                maxi = max(arr[i],maxi)
                continue
            else:
                arr[i] = maxi+1
                maxi = arr[i]
        maxi = max(maxi,arr[n-1])
        return maxi