import heapq
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums, k):
        n = len(nums)
        mp = defaultdict(int)
        pq = []

        for i in range(n):
            mp[nums[i]] += 1

        for x in mp.items():
            pq.append((-x[1], x[0]))

        heapq.heapify(pq)

        v = []
        while k > 0:
            v.append(heapq.heappop(pq)[1])
            k -= 1

        return v