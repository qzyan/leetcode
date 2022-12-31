class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        solution = [["."] * n for _ in range(n)]
        solutions = []
        cols = set()
        diags = set()
        anti_diags = set()
        self.backtrack(solution, solutions, 0, n, cols, diags, anti_diags)
        return solutions
        
    def backtrack(self, solution, solutions, row_idx, n, cols, diags, anti_diags):
        if row_idx == n:
            solutions.append(list(map(lambda eles: ''.join(eles), solution)))
            return
        
        for col_idx in range(n):
            if not self.possible(solution, row_idx, col_idx, n, cols, diags, anti_diags):
                solution[row_idx][col_idx] = '.'
                continue
            
            solution[row_idx][col_idx] = 'Q'
            cols.add(col_idx)
            diags.add(row_idx + col_idx)
            anti_diags.add(row_idx - col_idx)
            self.backtrack(solution, solutions, row_idx + 1, n, cols, diags, anti_diags)
            solution[row_idx][col_idx] = '.'
            cols.remove(col_idx)
            diags.remove(row_idx + col_idx)
            anti_diags.remove(row_idx - col_idx)
            
        return
    
    def possible(self, solution, row_ori, col_ori, n, cols, diags, anti_diags):
        diag = row_ori + col_ori
        anti_diag = row_ori - col_ori
        if col_ori in cols or diag in diags or anti_diag in anti_diags:
            return False
        
        return True
        
            
                
        