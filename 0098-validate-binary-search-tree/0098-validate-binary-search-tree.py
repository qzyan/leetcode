# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validBST_helper(root, -float("inf"), float("inf"))
    
    def validBST_helper(self, root, low, high):
        if root is None:
            return True
        if root.val >= high or root.val <= low:
            return False
        if not self.validBST_helper(root.left, low, root.val):
            return False
        if not self.validBST_helper(root.right, root.val, high):
            return False
        
        return True