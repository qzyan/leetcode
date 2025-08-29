class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                new_node = TrieNode()
                node.children[char] = new_node
            
            node = node.children[char]

        node.is_word = True
        node.word = word

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = ""

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = self.build_trie(words)
        node = trie.root

        visited = set()
        results = set()
        for row_idx in range(len(board)):
            for col_idx in range(len(board[0])):
                char = board[row_idx][col_idx]
                if char not in node.children:
                    continue
                
                visited.add((row_idx, col_idx))
                self.dfs(board, row_idx, col_idx, node.children[char], visited, results)
                visited.remove((row_idx, col_idx))

        return list(results)

    def build_trie(self, words):
        trie = Trie()
        for word in words:
            trie.add(word)

        return trie

    def dfs(self, board, row_idx, col_idx, node, visited, results):
        if node.is_word:
            results.add(node.word)
        
        if not node.children:
            return
        
        for next_row, next_col in self.get_neighbors(board, row_idx, col_idx):
            if (next_row, next_col) in visited:
                continue
            
            char = board[next_row][next_col]
            if char not in node.children:
                continue
            
            visited.add((next_row, next_col))
            self.dfs(board, next_row, next_col, node.children[char], visited, results)
            visited.remove((next_row, next_col))

    def get_neighbors(self, board, row_idx, col_idx):
        neighbors = []
        for d_row, d_col in DIRECTIONS:
            next_row, next_col = d_row + row_idx, d_col + col_idx
            if 0 <= next_row < len(board) and 0 <= next_col < len(board[0]):
                neighbors.append((next_row, next_col))

        return neighbors

DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]