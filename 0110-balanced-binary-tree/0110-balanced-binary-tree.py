# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        height, is_balanced = self.isBalanced_helper(root)
        return is_balanced
    
    def isBalanced_helper(self, root):
        if not root:
            return 0, True
        
        left_height, is_left_balanced = self.isBalanced_helper(root.left)
        right_height, is_right_balanced = self.isBalanced_helper(root.right)
        height = max(left_height, right_height) + 1
        
        if not is_left_balanced or not is_right_balanced:
            return height, False
        
        return height, abs(left_height - right_height) <= 1
        