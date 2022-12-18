# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.flatten_return_last_node(root)
        return root
    
    def flatten_return_last_node(self, root):
        if not root:
            return None
        
        left_last_node = self.flatten_return_last_node(root.left)
        right_last_node = self.flatten_return_last_node(root.right)

        if left_last_node:
            left_last_node.right = root.right
            root.right = root.left
            root.left = None

        return right_last_node or left_last_node or root
        