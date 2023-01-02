import collections

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        word_dict = set(wordList)
        if endWord not in word_dict:
            return []
        
        graph = self.build_graph(beginWord, endWord, word_dict)
        print(graph)
        if graph is None:
            return []
        
        path = [beginWord]
        paths = []
        not_viable = set()
        self.backtrack(graph, path, paths, not_viable, endWord)
        
        return paths
    
    def backtrack(self, graph, path, paths, not_viable, endWord):
        if path[-1] in not_viable:
            return False
            
        if path[-1] == endWord:
            paths.append(path[:])
            return True
        
        curr_word = path[-1]
        neighbors = graph.get(curr_word, [])
        can_reach_endword = False
        for neighbor in neighbors:
            path.append(neighbor)
            if self.backtrack(graph, path, paths, not_viable, endWord):
                can_reach_endword = True
            path.pop()
        
        if not can_reach_endword:
            not_viable.add(curr_word)
        
        return can_reach_endword
    
    def build_graph(self, beginWord, endWord, word_dict):
        distance = {
            beginWord: 0
        }
        queue = collections.deque([beginWord])
        graph = {}
        
        while queue:
            size = len(queue)
            for _ in range(size):
                curr_word = queue.popleft()
                if curr_word == endWord:
                    return graph                    
                graph[curr_word] = []
                next_words = self.find_neighbors(curr_word, word_dict)
                for next_word in next_words:
                    # next_word never visited before
                    # add to queue
                    if next_word not in distance:
                        queue.append(next_word)
                        distance[next_word] = distance[curr_word] + 1
                        graph[curr_word].append(next_word)
                        continue
                    # next_word has been visited and is on the next level
                    # do not append to queue but add to the graph[curr_word] neighbors
                    if distance[next_word] == distance[curr_word] + 1:
                        graph[curr_word].append(next_word)
                                
        return None
    
    def find_neighbors(self, curr_word, word_dict):
        neighbors = []
        for idx in range(len(curr_word)):
            for char in 'abcdefghijklmnopqrstuvwxyz':
                if char == curr_word[idx]:
                    continue
                new_word = curr_word[:idx] + char + curr_word[idx + 1:]
                if new_word in word_dict:
                    neighbors.append(new_word)
                    
        return neighbors