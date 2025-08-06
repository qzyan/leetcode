class Solution:
    def getMoneyAmount(self, n: int) -> int:
        if n <= 1:
            return 0

        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for row in range(n, 0, -1):
            for col in range(row + 1, n + 1):
                dp[row][col] = self.calc_cost(dp, row, col)

        return dp[1][n]

    def calc_cost(self, dp, row, col):
        min_cost = float("inf")
        for i in range(row, col):
            cost = i + max(dp[row][i - 1], dp[i + 1][col])
            min_cost = min(min_cost, cost)

        return min_cost