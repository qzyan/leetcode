class GridType:
    DEAD = 0
    LIVE = 1
    DEADTOLIVE = 2
    LIVETODEAD = 3

DIRECTIONS = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        if not board or not board[0]:
            return

        for row in range(len(board)):
            for col in range(len(board[0])):
                live_count, dead_count = self.count_surrounding_cells(board, row, col)
                if board[row][col] == GridType.LIVE and live_count < 2:
                    board[row][col] = GridType.LIVETODEAD

                if board[row][col] == GridType.LIVE and live_count > 3:
                    board[row][col] = GridType.LIVETODEAD

                if board[row][col] == GridType.DEAD and live_count == 3:
                    board[row][col] = GridType.DEADTOLIVE

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == GridType.DEADTOLIVE:
                    board[row][col] = GridType.LIVE
                    
                if board[row][col] == GridType.LIVETODEAD:
                    board[row][col] = GridType.DEAD
    
    def count_surrounding_cells(self, board, row, col):
        live_count, dead_count = 0, 0
        for d_row, d_col in DIRECTIONS:
            n_row, n_col = d_row + row, d_col + col
            if n_row < 0 or n_row >= len(board) or n_col < 0 or n_col >= len(board[0]):
                continue

            if board[n_row][n_col] == GridType.LIVE or board[n_row][n_col] == GridType.LIVETODEAD:
                live_count += 1

            if board[n_row][n_col] == GridType.DEAD or board[n_row][n_col] == GridType.DEADTOLIVE:
                dead_count += 1
        
        return live_count, dead_count


                
