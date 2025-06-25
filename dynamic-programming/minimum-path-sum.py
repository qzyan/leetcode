class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [0] * len(grid[0])
        dp[0] = grid[0][0]
        for i in range(1, len(grid[0])):
            dp[i] = dp[i - 1] + grid[0][i]

        for row in range(1, len(grid)):
            dp[0] = dp[0] + grid[row][0]
            for col in range(1, len(grid[0])):
                dp[col] = min(dp[col], dp[col - 1]) + grid[row][col]

        return dp[-1]