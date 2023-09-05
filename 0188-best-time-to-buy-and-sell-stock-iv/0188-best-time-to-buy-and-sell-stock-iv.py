class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        def solve(ind,buy,cap):
            if ind==n or cap==0:
                return 0
            if dp[ind][buy][cap]!=-1:
                return dp[ind][buy][cap]
            profit=0
            if buy==0:
                take=-prices[ind]+solve(ind+1,1,cap)
                not_take=0+solve(ind+1,0,cap)
                profit=max(take,not_take)
            else:
                take=prices[ind]+solve(ind+1,0,cap-1)
                not_take=0+solve(ind+1,1,cap)
                profit=max(take,not_take)
            dp[ind][buy][cap]=profit
            return dp[ind][buy][cap]
        n=len(prices)
        dp=[[[ -1 for _ in range(k+1)] for _ in range(2)] for _ in range(n)]
        return solve(0,0,k)