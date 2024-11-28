# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        is_p_found, is_q_found, lca = self.lca_helper(root, p, q)
        
        return lca
    
    def lca_helper(self, root, p, q):
        if root is None:
            return False, False, None
        
        is_p_found_in_left, is_q_found_in_left, left_lca = self.lca_helper(root.left, p, q)
        is_p_found_in_right, is_q_found_in_right, right_lca = self.lca_helper(root.right, p, q)
        
        is_p_found = is_p_found_in_left or is_p_found_in_right or root == p
        is_q_found = is_q_found_in_left or is_q_found_in_right or root == q
        
        lca = None
        if is_p_found and is_q_found:
            lca = left_lca or right_lca or root
        
        return is_p_found, is_q_found, lca

        
        
        