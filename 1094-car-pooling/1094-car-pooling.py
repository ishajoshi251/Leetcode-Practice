class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        maxi = 0
        for i in range(len(trips)):
            maxi = max(maxi,trips[i][2])
        arr = [0]*maxi
        for i in range(len(trips)):
            for j in range(trips[i][1],trips[i][2]):
                arr[j] += trips[i][0]
        if max(arr)>capacity:
            return False
        else:
            return True
            
        