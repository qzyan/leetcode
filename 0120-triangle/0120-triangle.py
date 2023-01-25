class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp  = [[0]* (i + 1) for i in range(n)]
        
        
        for idx in range(n):
            dp[n - 1][idx] = triangle[n - 1][idx]
            
        for row_idx in range(n - 2, -1, -1):
            for col_idx in range(row_idx + 1):
                dp[row_idx][col_idx] = triangle[row_idx][col_idx] + min(dp[row_idx + 1][col_idx], dp[row_idx + 1][col_idx + 1])
        
        return dp[0][0]
            