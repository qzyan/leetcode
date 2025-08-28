class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = TrieNode() 
                node.children[char] = new_node
                node = new_node

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
        words = set(words)
        path = []
        paths = []
        visited = set()
        for row_idx in range(len(board)):
            for col_idx in range(len(board[0])):
                curr_char = board[row_idx][col_idx]
                if curr_char not in node.children:
                    continue

                path.append(curr_char)
                visited.add((row_idx, col_idx))
                self.dfs(path, paths, row_idx, col_idx, visited, node.children[curr_char], board, words)
                path.pop()
                visited.remove((row_idx, col_idx))

        return list(set(paths))

    def build_trie(self, words):
        trie = Trie()
        for word in words:
            trie.add(word)
        
        return trie

    def dfs(self, path, paths, row_idx, col_idx, visited, node, board, words):
        curr_word = "".join(path)
        if curr_word in words:
            paths.append(curr_word)

        for next_row, next_col in self.get_neighbors(row_idx, col_idx, board):
            if (next_row, next_col) in visited:
                continue
            
            next_char = board[next_row][next_col]
            if next_char in node.children:
                path.append(next_char)
                visited.add((next_row, next_col))
                self.dfs(path, paths, next_row, next_col, visited, node.children[next_char], board, words)
                path.pop()
                visited.remove((next_row, next_col))

    def get_neighbors(self, row_idx, col_idx, board):
        neighbors = []
        for d_row, d_col in DIRECTIONS:
            next_row, next_col = d_row + row_idx, d_col + col_idx
            if 0 <= next_row < len(board) and 0 <= next_col < len(board[0]):
                neighbors.append((next_row, next_col))

        return neighbors


DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]


        

        
