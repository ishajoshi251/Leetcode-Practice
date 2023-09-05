class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        def solve(ind,buy):
            if ind==n:
                return 0
            if dp[ind][buy]!=-1:
                return dp[ind][buy]
            profit=0
            if buy==0: #buy a stock
                take=-prices[ind]+solve(ind+1,1) 
                not_take=0+solve(ind+1,0)
                profit=max(take,not_take)
            else:
                take=prices[ind]-fee+solve(ind+1,0) 
                not_take=0+solve(ind+1,1)
                profit=max(take,not_take)
            dp[ind][buy]=profit
            return dp[ind][buy]
        n=len(prices)
        dp=[[-1,-1] for i in range(n)]
        return solve(0,0)
    