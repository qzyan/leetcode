class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        # graph = [[p, q, r], [...], [neighbors]]
        graph = self.build_graph(n, edges)
        counts = [0] * n
        visited = set([0])
        node_labelcount = [{char: 0 for char in 'abcdefghijklmnopqrstuvwxyz'} for _ in range(n)]
        self.count_helper(graph, labels, 0, counts, visited, node_labelcount)

        return counts
    
    def build_graph(self, n, edges):
        graph = [[] for _ in range(n)]
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
            
        return graph
    
    def count_helper(self, graph, labels, curr_node, counts, visited, node_labelcount):
        for neighbor in graph[curr_node]:
            if neighbor in visited:
                continue
            
            visited.add(neighbor)
            self.count_helper(graph, labels, neighbor, counts, visited, node_labelcount)
            visited.discard(neighbor)
        
        curr_label = labels[curr_node]
        node_labelcount[curr_node][curr_label] += 1
        
        for neighbor in graph[curr_node]:
            neighbor_labelcount = node_labelcount[neighbor]
            for label, count in neighbor_labelcount.items():
                node_labelcount[curr_node][label] += count
        
        counts[curr_node] += node_labelcount[curr_node][curr_label]
            