# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_seq_sum, max_path_sum = self.helper(root)
        return max_path_sum

    # root is not None
    def helper(self, root):
        if not root.left and not root.right:
            return root.val, root.val

        if root.left:
            left_max_seq_sum, left_max_path_sum = self.helper(root.left)
        else:
            left_max_seq_sum, left_max_path_sum = -float("inf"), -float("inf")
        
        if root.right:
            right_max_seq_sum, right_max_path_sum = self.helper(root.right)
        else:
            right_max_seq_sum, right_max_path_sum = -float("inf"), -float("inf")
        
        # if < 0, do not add to the seq
        left_max_seq_sum = max(0, left_max_seq_sum)
        right_max_seq_sum = max(0, right_max_seq_sum)
        max_seq_sum = root.val + max(left_max_seq_sum, right_max_seq_sum)

        # choose of the path in left/right
        max_path_sum = max(right_max_path_sum, left_max_path_sum)
        max_path_sum = max(max_path_sum, root.val + left_max_seq_sum + right_max_seq_sum)

        return max_seq_sum, max_path_sum