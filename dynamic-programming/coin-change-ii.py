class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]
        for row in range(len(dp)):
            dp[row][0] = 1

        for row in range(1, len(dp)):
            for col in range(1, len(dp[0])):
                coin = coins[row - 1]
                dp[row][col] = dp[row - 1][col] + (dp[row][col - coin] if col - coin >= 0 else 0)

        return dp[-1][-1]