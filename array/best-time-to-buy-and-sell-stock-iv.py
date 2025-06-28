class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp1 = [0] * len(prices)
        for _ in range(1, k + 1):
            dp2 = [0] * len(prices)
            max_after_buy = -float("inf")
            for idx, price in enumerate(prices):
                max_after_buy = max(max_after_buy, dp1[idx] - price)
                dp2[idx] = max(dp2[idx - 1], max_after_buy + price)

            dp1 = dp2

        return dp1[-1]

