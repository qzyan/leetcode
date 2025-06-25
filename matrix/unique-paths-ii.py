class GridType:
    EMPTY = 0
    BLOCK = 1

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        
        dp = [0] * len(obstacleGrid[0])
        dp[0] = 1 if obstacleGrid[0][0] == GridType.EMPTY else 0
        for i in range(1, len(dp)):
            if obstacleGrid[0][i] == GridType.BLOCK:
                dp[i] = 0
            else:
                dp[i] = 1

        for row in range(1, len(obstacleGrid)):
            if obstacleGrid[row][0] == GridType.BLOCK:
                dp[0] = 0
            for col in range(1, len(obstacleGrid[0])):
                if obstacleGrid[row][col] == GridType.BLOCK:
                    dp[col] = 0
                else:
                    dp[col] = dp[col] + dp[col - 1]

        return dp[-1]