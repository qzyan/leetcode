# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        # if p has right sub tree
            # return the leftmost of the subtree
        # init a stack
        # find the path to the p
        # pop nodes from stack
        # return the first node whose val > p
        # if no node.val > p.val, return None
        if p.right:
            node = p.right
            while node.left:
                node = node.left
            return node
        
        path = self.get_path_to_target(root, p)
        while path:
            node = path.pop()
            if node.val > p.val:
                return node
        
        return None
    
    def get_path_to_target(self, root, target):
        path = [root]
        node = root
        
        while node != target:
            if node.val > target.val:
                node = node.left
            else:
                node = node.right
                
            path.append(node)
        
        return path