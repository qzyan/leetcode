# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.helper(root, 0)

    def helper(self, root, curr_sum):
        if not root:
            return 0

        curr_sum = curr_sum * 10 + root.val
        if not root.left and not root.right:
            return curr_sum

        left_res = self.helper(root.left, curr_sum)
        right_res = self.helper(root.right, curr_sum)

        return left_res + right_res