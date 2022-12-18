# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        has_p, has_q, lca = self.lca_helper(root, p, q)
        return lca

    # return if the root tree contains p, q, and the common ancestor 
    # (cotain_p, contain_q, ca)
    def lca_helper(self, root, p, q):
        if root is None:
            return False, False, None
        
        left_has_p, left_has_q, left_lca = self.lca_helper(root.left, p, q)
        # left sub tree contains lca
        if left_has_p and left_has_q:
            return True, True, left_lca
        
        right_has_p, right_has_q, right_lca = self.lca_helper(root.right, p, q)
        # right sub tree contains lca
        if right_has_p and right_has_q:
            return True, True, right_lca
        
        has_p = right_has_p or left_has_p or root == p
        has_q = right_has_q or left_has_q or root == q
        lca = None
        if has_p and has_q:
            lca = root
        
        return has_p, has_q, lca
         

        



