class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[float("inf")] * len(grid[0]) for _ in range(len(grid))]
        dp[0][0] = grid[0][0]
        for i in range(1, len(grid[0])):
            dp[0][i] = dp[0][i - 1] + grid[0][i]
        
        for i in range(1, len(grid)):
            dp[i][0] = dp[i - 1][0] + grid[i][0]

        for row in range(1, len(grid)):
            for col in range(1, len(grid[0])):
                dp[row][col] = min(dp[row - 1][col], dp[row][col - 1]) + grid[row][col]

        return dp[-1][-1]