class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = ""

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
                continue
            
            new_node = TrieNode()
            node.children[char] = new_node
            node = new_node

        node.word = word
        node.is_word = True

class WordDictionary:
    def __init__(self):
        self.trie = Trie()
        
    def addWord(self, word: str) -> None:
        self.trie.add(word)

    def search(self, word: str) -> bool:
        node = self.trie.root

        return self.helper(node, word, 0)

    def helper(self, node, word, start_idx):
        for idx in range(start_idx, len(word)):
            char = word[idx]
            if char != ".":
                if char in node.children:
                    node = node.children[char]
                else:
                    return False
            else:
                for next_char, next_node in node.children.items():
                    if self.helper(next_node, word, idx + 1):
                        return True
                
                return False

        return node.is_word      



        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)