class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = self.build_graph(equations, values)
        return [self.dfs(q[0], q[1], set(), graph) for q in queries]

    def dfs(self, start, end, visited, graph):
        if graph[start][end] != 0.0:
            return graph[start][end]
        
        visited.add(start)
        for next_char in graph[start]:
            if next_char in visited:
                continue

            sub_res = self.dfs(next_char, end, visited, graph)
            if sub_res != -1.0:
                return sub_res * graph[start][next_char]
        
        visited.remove(start)
        
        return -1.0
        

    def build_graph(self, equations, values):
        graph = defaultdict(lambda :defaultdict(float))
        for idx in range(len(equations)):
            char1, char2 = equations[idx]
            value = values[idx]

            graph[char1][char2] = value
            graph[char2][char1] = 1 / value
            graph[char1][char1] = 1.0
            graph[char2][char2] = 1.0


        return graph