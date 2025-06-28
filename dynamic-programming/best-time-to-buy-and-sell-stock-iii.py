class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp1 = [0] * len(prices) # util idx day, with n     trade, max profit can get
        dp2 = [0] * len(prices) # util idx day, with n + 1 trade, max profit can get
        
        for _ in range(2):
            max_after_buy = -float("inf")
            for idx, price in enumerate(prices):
                max_after_buy = max(max_after_buy, dp1[idx] - price)
                dp2[idx] = max(dp2[idx - 1], max_after_buy + price) if idx - 1 >= 0 else 0

            dp1 = dp2
            dp2 = [0] * len(prices)

        return dp1[-1]