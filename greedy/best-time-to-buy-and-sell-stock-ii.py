class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        hold = -prices[0]
        nohold = 0

        for i in range(1, len(prices)):
            hold = max(hold, nohold - prices[i])
            nohold = max(nohold, hold + prices[i])

        return nohold