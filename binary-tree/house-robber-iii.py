# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        rob_root_max, no_rob_root_max = self.rob_helper(root)
        return max(rob_root_max, no_rob_root_max)

    def rob_helper(self, root):
        if root is None:
            return (0, 0)

        l_rob_root_max, l_no_rob_root_max = self.rob_helper(root.left)
        r_rob_root_max, r_no_rob_root_max = self.rob_helper(root.right)

        rob_root_max = root.val + l_no_rob_root_max + r_no_rob_root_max
        no_rob_root_max = l_rob_root_max + r_rob_root_max
        return (rob_root_max, no_rob_root_max)
