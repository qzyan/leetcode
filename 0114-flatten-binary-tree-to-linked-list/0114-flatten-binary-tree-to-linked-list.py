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
        while root:
            left = root.left
            if left is None:
                root = root.right
                continue
            
            left_rightest = self.find_rightest(left)
            left_rightest.right = root.right
            root.right = root.left
            root.left = None
            root = root.right
            
    def find_rightest(self, root):
        while root.right:
            root = root.right
            
        return root
            
            
            
            