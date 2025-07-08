class Solution:
    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
        graph = self.build_graph(edges)
        visited = set([0])
        memo = [[None] * 14 for _ in range(len(coins))]
        res = self.dfs(graph, coins, 0, 0, visited, k, memo)
        return res

    def dfs(self, graph, coins, root, reduced_times, visited, k, memo):
        if memo[root][reduced_times] is not None:
            return reduced_times
        if reduced_times > 14:
            return 0

        curr_coin = coins[root] >> reduced_times

        res1 = curr_coin - k
        for neighbor in graph[root]:
            if neighbor in visited:
                continue
            
            visited.add(neighbor)
            sub_res1 = self.dfs(graph, coins, neighbor, reduced_times, visited, k, memo)
            visited.remove(neighbor)
            res1 += sub_res1
        
        if curr_coin - k > curr_coin // 2:
            memo[root][reduced_times] = res1
            return res1
        
        res2 = curr_coin // 2
        for neighbor in graph[root]:
            if neighbor in visited:
                continue
            
            visited.add(neighbor)
            sub_res2 = self.dfs(graph, coins, neighbor, reduced_times + 1, visited, k, memo)
            visited.remove(neighbor)
            res2 += sub_res2

        memo[root][reduced_times] = max(res1, res2)
        return max(res1, res2)
    
    def build_graph(sefl, edges):
        graph = {}
        for n1, n2 in edges:
            graph[n1] = graph.get(n1, set())
            graph[n2] = graph.get(n2, set())
            graph[n1].add(n2)
            graph[n2].add(n1)
        
        return graph
