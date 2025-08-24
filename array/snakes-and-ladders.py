class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        queue = deque([1])
        visited = set([1])

        step = 0
        while queue:
            for _ in range(len(queue)):
                curr_idx = queue.popleft()
                if curr_idx == n ** 2:
                    return step

                for i in range(1, 7):
                    next_idx = curr_idx + i
                    if next_idx > n ** 2:
                        continue

                    if next_idx in visited:
                        continue
                    
                    row, col = self.get_pos(board, next_idx)
                    if board[row][col] != -1:
                        queue.append(board[row][col])
                    else:
                        queue.append(next_idx)
                        visited.add(next_idx)
                
            step += 1

        return -1



        return self.dfs(1, board, {})

    def get_pos(self, board, square_idx):
        start_row = len(board) - 1
        start_col = 0
        row_idx = start_row - (square_idx - 1) // len(board)

        col_idx = (square_idx - 1) % len(board) if (square_idx - 1) // len(board) % 2 == 0 else len(board) - 1 - (square_idx - 1) % len(board)
        return row_idx, col_idx