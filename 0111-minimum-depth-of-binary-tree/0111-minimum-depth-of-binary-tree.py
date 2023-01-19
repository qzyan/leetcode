# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        if root.left is None and root.right is None:
            return 1
        
        child_min_depth = float('inf')
        if root.left is not None:
            child_min_depth = min(self.minDepth(root.left), child_min_depth)
        if root.right is not None:
            child_min_depth = min(self.minDepth(root.right), child_min_depth)
        
        return child_min_depth + 1