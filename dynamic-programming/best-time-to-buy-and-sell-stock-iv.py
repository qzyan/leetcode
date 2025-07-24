class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0

        buys = [-prices[0]] * (k + 1)
        buys[0] = 0
        sells = [0] * (k + 1)
        for idx in range(1, len(prices)):
            price = prices[idx]
            for j in range(1, k + 1):
                buys[j] = max(buys[j], sells[j - 1] - price)
                sells[j] = max(sells[j], buys[j] + price)
        
        return sells[-1]