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
        
        vals.append(root.val)
        self.dfs(root.left, vals)
        self.dfs(root.right, vals)
        