class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        dp = [0] * n 

        min_price = prices[0]

        for i in range(1,n):
            min_price = min(prices[i] , min_price)
            dp[i] = max(dp[i-1] , prices[i] - min_price)

        return(dp[n-1])