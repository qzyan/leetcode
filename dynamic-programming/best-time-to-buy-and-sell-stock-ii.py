class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_after_buy = -float("inf")
        max_after_sell = 0

        for price in prices:
            max_after_buy = max(max_after_sell - price, max_after_buy)
            max_after_sell = max(max_after_buy + price, max_after_sell)

        return max_after_sell