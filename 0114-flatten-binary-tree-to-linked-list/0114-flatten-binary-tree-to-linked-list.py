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
        # iterate over each node -> node.right
            # if node has no left node, continue
            # find the right_most of the left node
            # append the right node to right_most.right
            # node.right = node.left
            # node.left = None
        
        while root:
            if root.left is None:
                root = root.right
                continue
            
            node = root.left
            while node.right:
                node = node.right
            node.right = root.right
            
            root.right = root.left
            root.left = None
            
            root = root.right