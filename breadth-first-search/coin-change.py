class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        coin_set = set(coins)
        for i in range(1, len(dp)):
            if i in coin_set:
                dp[i] = 1
                continue

            for j in range(1, i // 2 + 1):
                if dp[j] == -1 or dp[i - j] == -1:
                    continue
                
                dp[i] = min(dp[i], dp[j] + dp[i - j])

        return dp[amount] if dp[amount] != float("inf") else -1
                

                
