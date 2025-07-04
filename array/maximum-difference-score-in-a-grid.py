class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        dp = [[float("inf")] * len(grid[0]) for _ in range(len(grid))]
        res = -float("inf")
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                prev_min = min(dp[row - 1][col] if row else float("inf"), dp[row][col - 1] if col else float("inf"))
                dp[row][col] = min(grid[row][col], prev_min) 
                res = max(res, grid[row][col] - prev_min)

        return res