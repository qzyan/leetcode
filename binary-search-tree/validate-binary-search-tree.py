# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        is_bst, _, _ = self.helper(root)

        return is_bst

    def helper(self, root):
        if not root:
            return True, -float("inf"), float("inf")

        is_l_bst, l_max, l_min = self.helper(root.left)
        is_r_bst, r_max, r_min = self.helper(root.right)

        is_bst = is_l_bst and is_r_bst and l_max < root.val and r_min > root.val
        max_val = r_max if r_max != -float("inf") else root.val
        min_val = l_min if l_min != float("inf") else root.val

        return is_bst, max_val, min_val
