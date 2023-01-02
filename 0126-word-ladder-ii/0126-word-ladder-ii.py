import collections

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        word_dict = set(wordList)
        if endWord not in word_dict:
            return []

        graph = self.build_graph(beginWord, endWord, word_dict)
        if not graph:
            return []
        
        path = [beginWord]
        paths = []
        not_viable = set()
        self.backtrack(path, paths, endWord, graph, not_viable)
        return paths
    
    def backtrack(self, path, paths, endWord, graph, not_viable):
        word = path[-1]
        if word == endWord:
            paths.append(path[:])
            return True
        if word in not_viable:
            return False
        
        find_end_word = False
        neighbors = graph.get(word, [])
        for neighbor in neighbors:
            path.append(neighbor)
            if self.backtrack(path, paths, endWord, graph, not_viable):
                find_end_word = True
            path.pop()
        
        if not find_end_word:
            not_viable.add(word)
        return find_end_word
            
    def build_graph(self, beginWord, endWord, word_dict):
        graph = {}
        queue = collections.deque([beginWord])
        word_dict_copy = set(word_dict)
        word_dict_copy.discard(beginWord)
        find_end_word = False
        
        while queue:
            size = len(queue)
            next_level_words = set()
            # iterate over each word on curr level, add the neighbor to the graph[curr]
            for _ in range(size):
                curr = queue.popleft()
                graph[curr] = []
                
                neighbors = self.get_neighbors(curr, word_dict_copy)
                for neighbor in neighbors:
                    graph[curr].append(neighbor)
                    next_level_words.add(neighbor)
            
            # endWord is in the next level
            if endWord in next_level_words:
                find_end_word = True
                break
            
            # discard all the words on the next level from the dict
            # append the next_level_nodes to the queue
            for word in next_level_words:
                word_dict_copy.discard(word)
                queue.append(word)
        
        if not find_end_word:
            return None
        return graph
    
    def get_neighbors(self, word, word_dict_copy):
        neighbors = []
        for idx in range(len(word)):
            for char in 'abcdefghijklmnopqrstuvwxyz':
                new_word = word[:idx] + char + word[idx + 1:]
                if new_word in word_dict_copy:
                    neighbors.append(new_word)
        
        return neighbors