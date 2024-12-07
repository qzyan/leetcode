# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        
        if root == p:
            return p
        
        if root == q:
            return q
        
        left_result = self.lowestCommonAncestor(root.left, p , q)
        right_result = self.lowestCommonAncestor(root.right, p , q)
        
        if left_result and right_result:
            return root
        
        if not left_result and not right_result:
            return None
        
        if left_result:
            return left_result
        
        if right_result:
            return right_result