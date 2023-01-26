class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row_size = len(obstacleGrid)
        col_size = len(obstacleGrid[0])
        
        # special case: [1]  -> the first position is an obstacle -> can never go anywhere
        if obstacleGrid[0][0] == 1:
            return 0
        
        # init the dp 
        # dp[i][j] --> the number of paths from (0,0) to (i, j)
        dp = [[0] * col_size for _ in range(row_size)]
        dp[0][0] = 1
        for col_idx in range(col_size):
            if obstacleGrid[0][col_idx] == 1:
                    break
                    
            dp[0][col_idx] = 1
        
        for row_idx in range(row_size):
            if obstacleGrid[row_idx][0] == 1:
                break
                
            dp[row_idx][0] = 1
            
        min_size = min(row_size, col_size)
        for idx in range(1, min_size):
            for col_idx in range(idx, col_size):
                if obstacleGrid[idx][col_idx] == 1:
                    continue
                
                dp[idx][col_idx] = dp[idx - 1][col_idx] + dp[idx][col_idx - 1]
                
            for row_idx in range(idx, row_size):
                if obstacleGrid[row_idx][idx] == 1:
                    continue
                
                dp[row_idx][idx] = dp[row_idx - 1][idx] + dp[row_idx][idx - 1]
        
        return dp[-1][-1]