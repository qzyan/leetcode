class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        curr_min = float("inf")
        max_profit = 0
        for price in prices:
            if price < curr_min:
                curr_min = price
            else:
                max_profit = max(max_profit, price - curr_min)

        return max_profit

