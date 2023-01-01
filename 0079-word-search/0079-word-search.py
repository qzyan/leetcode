DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return False
        
        row_size = len(board)
        col_size = len(board[0])
        
        chars_set = set()
        for row_idx in range(row_size):
            for col_idx in range(col_size):
                chars_set.add(board[row_idx][col_idx])
                
        for char in word:
            if char not in chars_set:
                return False
            

        visited = [[False] * col_size for _ in range(row_size)]
        for row_idx in range(row_size):
            for col_idx in range(col_size):
                visited[row_idx][col_idx] = True
                if self.dfs(board, row_idx, col_idx, word, visited, 0):
                    return True
                visited[row_idx][col_idx] = False
        return False
    
    def dfs(self, board, row_idx, col_idx, word, visited, curr_idx):
        char = board[row_idx][col_idx]
        if char != word[curr_idx]:
            return False
        if curr_idx == len(word) - 1 and char == word[curr_idx]:
            return True
        
        for d_row, d_col in DIRECTIONS:
            nxt_row = row_idx + d_row
            nxt_col = col_idx + d_col
            nxt_pos = (nxt_row, nxt_col)
            
            if not self.is_inbound(nxt_pos, board):
                continue
            if visited[nxt_row][nxt_col]:
                continue
            
            visited[nxt_row][nxt_col] = True
            if self.dfs(board, nxt_row, nxt_col, word, visited, curr_idx + 1):
                return True
            visited[nxt_row][nxt_col] = False
        
        return False
    
    def is_inbound(self, nxt_pos, board):
        return 0 <= nxt_pos[0] < len(board) and 0 <= nxt_pos[1] < len(board[0])