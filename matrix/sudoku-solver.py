class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        digits_in_rows = [set() for _ in range(9)]
        digits_in_cols = [set() for _ in range(9)]
        digits_in_subboxs = [set() for _ in range(9)]
        empty_cells = self.get_digits_and_empty_cells(board, digits_in_rows, digits_in_cols, digits_in_subboxs)

        self.dfs(board, 0, empty_cells, digits_in_rows, digits_in_cols, digits_in_subboxs)

    def get_digits_and_empty_cells(self, board, digits_in_rows, digits_in_cols, digits_in_subboxs):
        empty_cells = []
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    empty_cells.append((r, c))
                else:
                    d = board[r][c]
                    curr_subbox = r // 3 * 3 + c // 3
                    digits_in_rows[r].add(d)
                    digits_in_cols[c].add(d)
                    digits_in_subboxs[curr_subbox].add(d)

        return empty_cells

    def dfs(self, board, curr_idx, empty_cells, digits_in_rows, digits_in_cols, digits_in_subboxs):
        if curr_idx == len(empty_cells):
            return True
        
        curr_row, curr_col = empty_cells[curr_idx]
        curr_subbox = curr_row // 3 * 3 + curr_col // 3
        for digit in range(1, 10):
            d = str(digit)
            if d in digits_in_rows[curr_row] or d in digits_in_cols[curr_col] or d in digits_in_subboxs[curr_subbox]:
                continue
            
            board[curr_row][curr_col] = d
            digits_in_rows[curr_row].add(d)
            digits_in_cols[curr_col].add(d)
            digits_in_subboxs[curr_subbox].add(d)
            
            if self.dfs(board, curr_idx + 1, empty_cells, digits_in_rows, digits_in_cols, digits_in_subboxs):
                return True
            
            digits_in_rows[curr_row].remove(d)
            digits_in_cols[curr_col].remove(d)
            digits_in_subboxs[curr_subbox].remove(d)

        return False

        

