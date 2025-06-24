class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coin_set = set(coins)
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coin_set:
                if i - coin >= 0 and dp[i - coin] != float("inf"):
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount]!= float("inf") else -1