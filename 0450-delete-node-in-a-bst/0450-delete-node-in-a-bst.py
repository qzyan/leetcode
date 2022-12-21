# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        father, node_to_delete = self.find_node(root, key)
        if node_to_delete is None:
            return root
        
        left = node_to_delete.left
        right = node_to_delete.right
        node_to_delete.left = None
        node_to_delete.right = None
        
        if right is None:
            top_node = left
        else:
            top_node = right
            left_most = right
            while left_most.left:
                left_most = left_most.left
            left_most.left = left
            
        if father is None:
            return top_node
        if father.val < key:
            father.right = top_node
        else:
            father.left = top_node
        return root
        
    def find_node(self, root, key):
        father = None
        while root:
            if root.val == key:
                return father, root
            father = root
            if root.val > key:
                root = root.left
            elif root.val < key:
                root = root.right
        return None, None