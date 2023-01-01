DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not board[0] or not words:
            return []
        
        row_size = len(board)
        col_size = len(board[0])
        word_max_len = self.get_max_len(words)
        words_set = set(words)
        prefixs_set = self.get_prefixs(words)
        path = []
        paths = []
        visited = set()
        for row_idx in range(row_size):
            for col_idx in range(col_size):
                pos = (row_idx, col_idx)
                visited.add(pos)
                path.append(board[row_idx][col_idx])
                self.backtrack(board, pos, path, paths, visited, word_max_len, words_set, prefixs_set)
                visited.remove(pos)
                path.pop()
        
        return list(set(paths))
        
    def backtrack(self, board, pos, path, paths, visited, word_max_len, words_set, prefixs):
        curr_word = ''.join(path)

        if curr_word in words_set:
            paths.append(curr_word)
        
        if curr_word not in prefixs:
            return
        if len(path) == word_max_len:
            return
        
        neighbors = self.get_neighbors(board, pos)
        for neighbor in neighbors:
            if neighbor in visited:
                continue
            neighbor_row_idx = neighbor[0]
            neighbor_col_idx = neighbor[1]
            visited.add(neighbor)
            path.append(board[neighbor_row_idx][neighbor_col_idx])
            self.backtrack(board, neighbor, path, paths, visited, word_max_len, words_set, prefixs)
            visited.remove(neighbor)
            path.pop()
        
        return
            
    def get_max_len(self, words):
        max_len = 0
        for word in words:
            max_len = max(max_len, len(word))
        return max_len
    
    def get_neighbors(self, board, pos):
        row_idx, col_idx = pos
        neighbors = []
        for d_row, d_col in DIRECTIONS:
            nxt_row = row_idx + d_row
            nxt_col = col_idx + d_col
            if 0 <= nxt_row < len(board) and 0 <= nxt_col < len(board[0]):
                neighbors.append((nxt_row, nxt_col))
        
        return neighbors
    
    def get_prefixs(self, words):
        prefixs = set()
        for word in words:
            for idx in range(len(word)):
                prefixs.add(word[:idx + 1])
                
        return prefixs
    
        # path record the backtrack path
        # paths record all the paths that is in the words
        # iterate over each cell of the board
            # add the word in neighbor to path
            # backtrack from the char in the cell
            # pop the word in neighbor to path
    
    # backtrack
    # if the current path is no longer able to form a word in words, return
    # if the path lenght is longer than the longest word in words, return
    # iterate over the neighbors of the current position
        # add the word in neighbor to path
        # backtrack the neighbor
        # pop the word in neighbor to path