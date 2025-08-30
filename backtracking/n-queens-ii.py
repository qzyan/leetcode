class Solution:
    def totalNQueens(self, n: int) -> int:
        visited_cols = set()
        visited_diags1 = set()
        visited_diags2 = set()

        return self.dfs(0, n, visited_cols, visited_diags1, visited_diags2)

    def dfs(self, curr_row, n, visited_cols, visited_diags1, visited_diags2):
        if curr_row == n:
            return 1

        count = 0
        for curr_col in range(n):
            if curr_col in visited_cols:
                continue
            
            if curr_row + curr_col in visited_diags1:
                continue
            
            if curr_row - curr_col in visited_diags2:
                continue
            
            visited_cols.add(curr_col)
            visited_diags1.add(curr_row + curr_col)
            visited_diags2.add(curr_row - curr_col)

            count += self.dfs(curr_row + 1, n, visited_cols, visited_diags1, visited_diags2)
            
            visited_cols.remove(curr_col)
            visited_diags1.remove(curr_row + curr_col)
            visited_diags2.remove(curr_row - curr_col)

        return count