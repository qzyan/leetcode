class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_after_1st_purchase = -float("inf")
        max_profit = 0

        for price in prices:
            max_after_1st_purchase = max(max_after_1st_purchase, -price)
            max_profit = max(max_profit, max_after_1st_purchase + price)

        return max_profit