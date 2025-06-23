# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        root_max, children_max = self.rob_helper(root)
        return root_max

    def rob_helper(self, root):
        if root is None:
            return (0, 0)

        l_root_max, l_children_max = self.rob_helper(root.left)
        r_root_max, r_children_max = self.rob_helper(root.right)

        root_max = max(l_children_max + r_children_max + root.val, l_root_max + r_root_max)
        children_max = l_root_max + r_root_max
        return (root_max, children_max)
