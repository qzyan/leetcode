class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        empty_cells = self.get_digits_and_empty_cells(board)

        self.dfs(board, 0, empty_cells)

    def get_digits_and_empty_cells(self, board):
        empty_cells = []
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    empty_cells.append((r, c))

        return empty_cells

    def dfs(self, board, curr_idx, empty_cells):
        if curr_idx == len(empty_cells):
            return True
        
        curr_row, curr_col = empty_cells[curr_idx]
        for digit in range(1, 10):
            d = str(digit)
            if not self.is_valid(d, board, curr_row, curr_col):
                continue
            
            board[curr_row][curr_col] = d
            
            if self.dfs(board, curr_idx + 1, empty_cells):
                return True
            
            board[curr_row][curr_col] = "."
            
        return False

    def is_valid(self, d, board, r, c):
        subbox_start_row = r // 3 * 3
        subbox_start_col = c // 3 * 3

        for idx in range(9):
            if board[r][idx] != "." and board[r][idx] == d:
                return False
            
            if board[idx][c] != "." and board[idx][c] == d:
                return False
            
            if board[subbox_start_row + idx // 3][subbox_start_col + idx % 3] != "." and board[subbox_start_row + idx // 3][subbox_start_col + idx % 3] == d:
                return False

        return True
            



        

