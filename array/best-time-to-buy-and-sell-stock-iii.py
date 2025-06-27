class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        dp1 = [0] * len(prices) # max_profit after 1st trans
        dp2 = [0] * len(prices) # max_profit after 2nd trans

        curr_min = prices[0]
        max_left_afer_2nd_buy = -float("inf")
        for idx, price in enumerate(prices):
            dp1[idx] = max(dp1[idx - 1], price - curr_min)
            if price < curr_min:
                curr_min = price
            
            max_left_afer_2nd_buy = max(max_left_afer_2nd_buy, dp1[idx] - price)

            dp2[idx] = max(dp2[idx - 1], max_left_afer_2nd_buy + price)

        return dp2[-1]
