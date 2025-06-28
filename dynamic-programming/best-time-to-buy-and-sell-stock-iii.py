class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_after_1st_buy = -float("inf")
        max_after_1st_sell = 0
        max_after_2nd_buy = -float("inf")
        max_after_2nd_sell = 0

        for price in prices:
            max_after_1st_buy = max(max_after_1st_buy, -price)
            max_after_1st_sell = max(max_after_1st_sell, max_after_1st_buy + price)
            max_after_2nd_buy = max(max_after_2nd_buy, max_after_1st_sell - price)
            max_after_2nd_sell = max(max_after_2nd_sell, max_after_2nd_buy + price)

        return max_after_2nd_sell