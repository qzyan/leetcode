class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        dp = [[0] * n for _ in range(3)]
        for k in range(1, 3):
            max_after_buy = -float("inf")
            for i in range(n):
                max_after_buy = max(max_after_buy, dp[k - 1][i] - prices[i])
                dp[k][i] = max(dp[k][i - 1], max_after_buy + prices[i])

        return dp[-1][-1]