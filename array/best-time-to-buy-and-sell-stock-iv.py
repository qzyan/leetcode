class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k == 0:
            return 0
        if not prices:
            return 0

        dp = [[0] * len(prices) for _ in range(k + 1)]
        for row in range(1, k + 1):
            max_after_rowth_buy = -float("inf")
            for col in range(len(prices)):
                max_after_rowth_buy = max(max_after_rowth_buy, dp[row - 1][col] - prices[col])
                if col - 1 >= 0:
                    dp[row][col] = max(dp[row][col - 1], max_after_rowth_buy + prices[col])
                    
        return dp[k][len(prices) - 1]