#User function Template for python3

from typing import List

class Solution:
    def minimumMultiplications(self, arr: List[int], start: int, end: int) -> int:
        if start == end:
            return 0
        queue = []
        queue.append((start,0))
        distance = [1e9]*100000
        distance[start]=0
        mod = 100000
        while queue:
            node,steps = queue.pop(0)
            for x in arr:
                num = (x*node)%mod
                if steps+1 < distance[num]:
                    distance[num] = steps+1
                    if num == end:
                        return steps + 1
                    queue.append((num,steps+1))
        return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        start, end = list(map(int,input().split()))
        obj=Solution()
        print(obj.minimumMultiplications(arr, start, end))
# } Driver Code Ends