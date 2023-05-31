class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        maxi = 0
        count = 0
        for i in range(len(trips)):
            maxi = max(maxi,trips[i][2])
        arr = [0]*(maxi+1)
        for i in range(len(trips)):
            arr[trips[i][1]] += trips[i][0]
            arr[trips[i][2]] -= trips[i][0]
        for i in range(len(arr)):
            count += arr[i]
            if count>capacity:
                return False
        return True
            
        