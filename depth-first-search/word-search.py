class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        prefixs = set([word[:i] for i in range(1, len(word) + 1)])
        visited = set()
        curr_word = ""
        for row_idx in range(len(board)):
            for col_idx in range(len(board[0])):
                char = board[row_idx][col_idx]
                if curr_word + char not in prefixs:
                    continue
                
                visited.add((row_idx, col_idx))

                if self.dfs(row_idx, col_idx, board, prefixs, curr_word + char, word, visited):
                    return True

                visited.remove((row_idx, col_idx))

        return False

    def dfs(self, row_idx, col_idx, board, prefixs, curr_word, word, visited):
        if curr_word == word:
            return True
        
        if len(curr_word) == len(word):
            return False
        
        for next_row, next_col in self.get_neighbors(board, row_idx, col_idx):
            if (next_row, next_col) in visited:
                continue

            char = board[next_row][next_col]
            if curr_word + char not in prefixs:
                continue
        
            visited.add((next_row, next_col))
            char = board[next_row][next_col]
            if self.dfs(next_row, next_col, board, prefixs, curr_word + char, word, visited):
                return True

            visited.remove((next_row, next_col))

    def get_neighbors(self, board, row_idx, col_idx):
        neighbors = []
        for d_row, d_col in DIRECTIONS:
            next_row, next_col = row_idx + d_row, col_idx + d_col
            if 0 <= next_row < len(board) and 0 <= next_col < len(board[0]):
                neighbors.append((next_row, next_col))

        return neighbors

DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            


