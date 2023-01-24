class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = [[None] * (i + 1) for i in range(len(triangle))]
        self.dfs(triangle, 0, 0, memo)
        print(memo)
        return memo[0][0]
        
    def dfs(self, triangle, row_idx, col_idx, memo):
        if memo[row_idx][col_idx] is not None:
            return memo[row_idx][col_idx]
        
        if row_idx == len(triangle) - 1:
            memo[row_idx][col_idx] = triangle[row_idx][col_idx]
            return triangle[row_idx][col_idx]
            
        next_row_idx = row_idx + 1
        next_col_idxs = [col_idx, col_idx + 1]
        
        left_min_sum = self.dfs(triangle, next_row_idx, next_col_idxs[0], memo)
        right_min_sum = self.dfs(triangle, next_row_idx, next_col_idxs[1], memo)
        
        memo[row_idx][col_idx] = min(left_min_sum, right_min_sum) + triangle[row_idx][col_idx]
        return memo[row_idx][col_idx]