import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []
        for i in range(len(nums)):
            heapq.heappush(heap,-nums[i])
        for i in range(k):
            a = heapq.heappop(heap)
        return -a
        