class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        tree = self.build_tree(parent)
        
        val_mapping = {
            "deepest_depth": 0
        }
        
        self.helper(tree, 0, s, val_mapping)
        
        return val_mapping["deepest_depth"]
    
    def build_tree(self, parent):
        tree = [[] for _ in range(len(parent))]
        
        for node, parent in enumerate(parent):
            if node == 0:
                continue
            tree[parent].append(node)
            
        return tree
    
    # return the deepest depth starting from the curr_node
    def helper(self, tree, curr_node, s, val_mapping):
        curr_char = s[curr_node]
        
        # leaf node
        if len(tree[curr_node]) == 0:
            val_mapping["deepest_depth"] = max(val_mapping["deepest_depth"], 1)
            return 1
        
        # get the deepest and sec_deepest depth of all the child nodes
        child_deepest = 0
        child_sec_deepest = 0
        for child in tree[curr_node]:
            child_char = s[child]
            # dfs the child node regardless the char
            child_depth = self.helper(tree, child, s, val_mapping)
            
            if child_char == curr_char:
                continue
                
            if child_depth > child_deepest:
                child_sec_deepest = child_deepest
                child_deepest = child_depth
            elif child_depth > child_sec_deepest:
                child_sec_deepest = child_depth
                
        curr_deepest_depth = child_deepest + child_sec_deepest + 1
        val_mapping["deepest_depth"] = max(val_mapping["deepest_depth"], curr_deepest_depth)
        
        return child_deepest + 1
        
            
            