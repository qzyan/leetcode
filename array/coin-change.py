class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        coin_set = set(coins)
        for i in range(1, len(dp)):
            if i in coin_set:
                dp[i] = 1
                continue

            for coin in coin_set:
                if i - coin < 0:
                    continue

                if dp[i - coin] == float("inf"):
                    continue
                
                dp[i] = min(dp[i], dp[i - coin] + 1)


        return dp[amount] if dp[amount] != float("inf") else -1
                

                
