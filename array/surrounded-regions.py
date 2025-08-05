class GridType:
    CONNECT = "O"
    SURROUND = "X"

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        if len(board) <= 2 or len(board[0]) <= 2:
            return

        visited = set()
        # mark all O reachable from boarder
        for col in range(len(board[0])):
            if board[0][col] == GridType.CONNECT:
                self.dfs(board, 0, col, visited)
            if board[len(board) - 1][col] == GridType.CONNECT:
                self.dfs(board, len(board) - 1, col, visited)
        
        for row in range(1, len(board) - 1):
            if board[row][0] == GridType.CONNECT:
                self.dfs(board, row, 0, visited)
            if board[row][len(board[0]) - 1] == GridType.CONNECT:
                self.dfs(board, row, len(board[0]) - 1, visited)
        
        print(visited)
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == GridType.CONNECT and (row, col) not in visited:
                    board[row][col] = GridType.SURROUND

    def dfs(self, board, curr_row, curr_col, visited):
        visited.add((curr_row, curr_col))

        for next_row, next_col in self.get_neighbors(board, curr_row, curr_col):
            if (next_row, next_col) in visited:
                continue
            
            self.dfs(board, next_row, next_col, visited)

    def get_neighbors(self, board, curr_row, curr_col):
        neighbors = []
        for d_r, d_c in DIRECTIONS:
            next_r, next_c = d_r + curr_row, d_c + curr_col
            if 0 <= next_r < len(board) and 0 <= next_c < len(board[0]):
                if board[next_r][next_c] == GridType.CONNECT:
                    neighbors.append((next_r, next_c))

        return neighbors

DIRECTIONS = ((1, 0), (0, 1), (-1, 0), (0, -1))
