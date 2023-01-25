class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        
        for col_idx in range(n):
            dp[0][col_idx] = 1
            
        for row_idx in range(m):
            dp[row_idx][0] = 1
        
        
        for start_idx in range(1, min(n,m)):
            for row_idx in range(start_idx, m):
                dp[row_idx][start_idx] = dp[row_idx - 1][start_idx] + dp[row_idx][start_idx - 1]
                
            for col_idx in range(start_idx + 1, n):
                dp[start_idx][col_idx] = dp[start_idx - 1][col_idx] + dp[start_idx][col_idx - 1]
                
        return dp[m - 1][n - 1]
                
            
        
        