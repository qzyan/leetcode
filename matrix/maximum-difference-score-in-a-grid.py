class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        dp = [[-float("inf")] * len(grid[0]) for _ in range(len(grid))]
        res = -float("inf")
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                for j in range(row):
                    diff = grid[row][col] - grid[j][col]
                    score = max(0, dp[j][col]) + diff
                    dp[row][col] = max(dp[row][col], score)
                
                for k in range(col):
                    diff = grid[row][col] - grid[row][k]
                    score = max(0, dp[row][k]) + diff
                    dp[row][col] = max(dp[row][col], score)

                res = max(res, dp[row][col])

        return res
                