class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        mini = prices[0]
        maxi = 0
        for i in range(1,len(prices)):
            maxi = max( prices[i]-mini,maxi)
            
            mini = min(mini,prices[i])
           
        return maxi
            