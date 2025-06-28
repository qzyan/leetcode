class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        buys = [-float("inf")] * (k + 1)
        sells = [0] * (k + 1)

        for price in prices:
            for i in range(1, k + 1):
                buys[i] = max(buys[i], sells[i - 1] - price)
                sells[i] = max(sells[i], buys[i] + price)

        return sells[k]