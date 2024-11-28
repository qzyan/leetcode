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
        self.helper(root)
        
    def helper(self, root):
        if root is None:
            return None
        
        if root.left is None and root.right is None:
            return root

        flattened_left_tail = self.helper(root.left)
        flattened_right_tail = self.helper(root.right)
         
        if root.left is None:
            return flattened_right_tail
        
        if root.right is None:
            root.right = root.left
            root.left = None
            return flattened_left_tail

        right_head = root.right
        root.right = root.left
        flattened_left_tail.right = right_head
        root.left = None
        
        return flattened_right_tail
        
        