class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        nohold = 0
        hold = -prices[0]
        for i in range(len(prices)):
            price = prices[i]
            hold = max(hold, nohold - price)
            nohold = max(nohold, hold + price)

        return max(hold, nohold)