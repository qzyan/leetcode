class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        tree = self.build_tree(parent)
        print(tree)
        node_depths_mapping = {node: [] for node in range(len(parent))}
        
        self.helper(tree, node_depths_mapping, 0, s)
        print(node_depths_mapping)
        deepest = 0
        
        for node in node_depths_mapping:
            deepest_depth = 1
            second_deepest_depth = 1
            for depth in node_depths_mapping[node]:
                if depth > deepest_depth:
                    second_deepest_depth = deepest_depth
                    deepest_depth = depth
                elif depth > second_deepest_depth:
                    second_deepest_depth = depth
            deepest = max(deepest, deepest_depth + second_deepest_depth - 1)
        
        return deepest
    
    def build_tree(self, parent):
        tree = [[] for _ in range(len(parent))]
        
        for node, parent in enumerate(parent):
            if node == 0:
                continue
            tree[parent].append(node)
            
        return tree
    
    def helper(self, tree, node_depths_mapping, curr_node, s):
        curr_char = s[curr_node]
        if len(tree[curr_node]) == 0:
            node_depths_mapping[curr_node].append(1)
            return
        
        for child in tree[curr_node]:
            child_char = s[child]
            
            self.helper(tree, node_depths_mapping, child, s)
            if child_char != curr_char:            
                child_deepest_depth = max(node_depths_mapping[child])
                node_depths_mapping[curr_node].append(1 + child_deepest_depth)
            else:
                node_depths_mapping[curr_node].append(1)
        
        
            
            