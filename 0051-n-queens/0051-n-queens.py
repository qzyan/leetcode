class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        solution = [["."] * n for _ in range(n)]
        solutions = [] 
        self.backtrack(solution, solutions, 0, n)
        return solutions
        
    def backtrack(self, solution, solutions, row_idx, n):
        if row_idx == n:
            solutions.append(list(map(lambda eles: ''.join(eles), solution)))
            return
        
        for col_idx in range(n):
            solution[row_idx][col_idx] = 'Q'
            if not self.possible(solution, row_idx, col_idx, n):
                solution[row_idx][col_idx] = '.'
                continue
            
            self.backtrack(solution, solutions, row_idx + 1, n)
            solution[row_idx][col_idx] = '.'
            
        return
    
    def possible(self, solution, row_ori, col_ori, n):
        for row_idx in range(row_ori):
            if solution[row_idx][col_ori] == 'Q':
                return False
            
        
        for row_idx in range(row_ori):
            col_idx = row_ori + col_ori - row_idx
            if self.inbound(row_idx, col_idx, n) and solution[row_idx][col_idx] == 'Q':
                return False
        
        for row_idx in range(row_ori):
            col_idx = row_idx - (row_ori - col_ori)
            if self.inbound(row_idx, col_idx, n) and solution[row_idx][col_idx] == 'Q':
                return False
        
        return True
            
    def inbound(self, row_idx, col_idx, n):
        return 0 <= row_idx < n and 0 <= col_idx < n 
        
            
                
        