# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None
        
        if root == p or root == q:
            return root
        
        left_result = self.lowestCommonAncestor(root.left, p, q)
        right_result = self.lowestCommonAncestor(root.right, p, q)
        
        if left_result and not right_result:
            return left_result
        
        if right_result and not left_result:
            return right_result
        
        if left_result and right_result:
            return root
        