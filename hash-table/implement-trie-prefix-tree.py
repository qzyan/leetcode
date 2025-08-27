class TrieNode:
    def __init__(self, char=""):
        self.children = {}
        self.is_word = False
        self.word = ""

class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        node = self.root

        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node

        node.is_word = True
        node.word = word

    def search(self, word: str) -> bool:
        node = self.root

        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return False
        
        return node.is_word

    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return False
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)