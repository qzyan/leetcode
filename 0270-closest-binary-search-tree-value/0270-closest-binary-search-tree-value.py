# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        if root is None:
            return None
        
        if root.val > target:
            subtree_closest = self.closestValue(root.left, target)
        else:
            subtree_closest = self.closestValue(root.right, target)
            
        if subtree_closest is None:
            return root.val
            
        return root.val if abs(root.val - target) < abs(subtree_closest - target) else subtree_closest