class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = self.build_graph(edges, succProb, n)
        visited = set()
        return self.dfs(start_node, end_node, graph, visited)

    def build_graph(self, edges, succProb, n):
        graph = {i: {} for i in range(n)}

        for i in range(len(edges)):
            from_node, to_node = edges[i]
            prob = succProb[i]
            graph[from_node][to_node] = prob

        return graph

    def dfs(self, curr_node, end_node, graph, visited):
        if curr_node == end_node:
            return 1
        
        visited.add(curr_node)

        res = 0
        for next_node in graph[curr_node]:
            if next_node in visited:
                continue

            sub_res = self.dfs(next_node, end_node, graph, visited)
            res = max(graph[curr_node][next_node] * sub_res, res)

        visited.remove(curr_node)

        return res

        
