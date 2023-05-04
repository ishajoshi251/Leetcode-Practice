class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        refund = []
        N = len(costs)//2
        minCost = 0
        for A, B in costs:
            refund.append(B - A)
            minCost += A
        refund.sort()
        for i in range(N):
            minCost += refund[i]
        return minCost
        