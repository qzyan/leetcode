# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        stack = [(root, -float("inf"), float("inf"))]
        
        while stack:
            curr, low, high = stack.pop()
            if curr.val >= high or curr.val <= low:
                return False
            
            if curr.right:
                stack.append((curr.right, curr.val, high))
            if curr.left:
                stack.append((curr.left, low, curr.val))
                
        return True