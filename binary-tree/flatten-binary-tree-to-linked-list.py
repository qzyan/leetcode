# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        result = root

        while root:
            left_node = root.left
            right_node = root.right
            if left_node:
                left_tail = self.find_right_most(left_node)
                root.right = left_node
                left_tail.right = right_node

            root.left = None
            root = root.right

        
        return result

    def find_right_most(self, node):
        while node.right:
            node = node.right

        return node
