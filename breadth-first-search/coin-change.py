class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        coins = sorted(coins)

        for idx in range(1, amount + 1):
            prev_res = float("inf")
            for coin in coins:
                if idx - coin >= 0:
                    prev_res = min(dp[idx - coin], prev_res)
            
            if prev_res != float("inf"):
                dp[idx] = prev_res + 1

        return dp[-1] if dp[-1] != float("inf") else -1
