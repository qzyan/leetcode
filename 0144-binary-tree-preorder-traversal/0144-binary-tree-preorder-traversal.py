# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        vals = []
        self.dfs(root, vals)
        return vals
        
    def dfs(self, root, vals):
        if root is None:
            return
        
        stack = [root]
        while stack:
            curr = stack.pop()
            vals.append(curr.val)
            
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)