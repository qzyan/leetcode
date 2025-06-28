class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        max_at_buys = [-float("inf")] * (k + 1)
        max_at_sells = [0] * (k + 1)
        for price in prices:
            for i in range(1, k + 1):
                max_at_buys[i] = max(max_at_sells[i - 1] - price, max_at_buys[i])
                max_at_sells[i] = max(max_at_buys[i] + price, max_at_sells[i])

        return max_at_sells[k]
