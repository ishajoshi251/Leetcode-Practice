class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        mini = 100000000
        maxi = 0
        for i in range(len(prices)):
            mini = min(mini,prices[i])
            if prices[i]>mini:
                maxi = max(maxi,prices[i]-mini)
        return maxi
        