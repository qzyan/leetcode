class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = self.build_graph(equations, values)
        results = []
        visited = set()
        for q in queries:
            visited.add(q[0])
            result = self.dfs(q[0], q[1], visited, graph)
            visited.remove(q[0])
            results.append(result)

        return results

    def dfs(self, start, end, visited, graph):
        if start not in graph:
            return -1.0

        if start == end:
            return 1.0
        
        if end in graph[start]:
            return graph[start][end]

        for next_word in graph[start]:
            if next_word in visited:
                continue
            
            visited.add(next_word)
            sub_res = self.dfs(next_word, end, visited, graph)
            visited.remove(next_word)

            if sub_res != -1.0:
                return sub_res * graph[start][next_word]
                    
        return -1.0

    def build_graph(self, equations, values):
        graph = defaultdict(lambda :defaultdict(float))
        for idx in range(len(equations)):
            word1, word2 = equations[idx]
            val = values[idx]

            graph[word1][word2] = val
            graph[word2][word1] = 1.0 / val

        return graph