import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        q = []
        for i in range(len(points)):
            heapq.heappush(q,[-math.sqrt(points[i][0]*points[i][0]+points[i][1]*points[i][1]),points[i]])
            if len(q)>k:
                heapq.heappop(q)
        ans = []
        
        while q:
            ans.append(heapq.heappop(q)[1])
           
        return ans
           