class Solution:
    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
        graph = self.build_graph(edges)
        visited = set([0])
        memo = {}
        return self.dfs(0, graph, coins, k, 0, visited, memo)

    def dfs(self, curr_node, graph, coins, k, op2_count, visited, memo):
        if (curr_node, op2_count) in memo:
            return memo[(curr_node, op2_count)]
        op1 = (coins[curr_node] >> op2_count) - k
        for next_node in graph[curr_node]:
            if next_node in visited:
                continue
            
            visited.add(next_node)
            op1 += self.dfs(next_node, graph, coins, k, op2_count, visited, memo)
            visited.remove(next_node)

        if (coins[curr_node] >> op2_count) - k >= (coins[curr_node] >> (op2_count + 1)):
            return op1
        
        op2 = coins[curr_node] >> (op2_count + 1)
        for next_node in graph[curr_node]:
            if next_node in visited:
                continue
            
            visited.add(next_node)
            op2 += self.dfs(next_node, graph, coins, k, op2_count + 1, visited, memo)
            visited.remove(next_node)

        memo[(curr_node, op2_count)] = max(op2, op1)
        return memo[(curr_node, op2_count)]

    def build_graph(self, edges):
        graph = {}
        for p1, p2 in edges:
            graph[p1] = graph.get(p1, set())
            graph[p1].add(p2)
            graph[p2] = graph.get(p2, set())
            graph[p2].add(p1)

        return graph

