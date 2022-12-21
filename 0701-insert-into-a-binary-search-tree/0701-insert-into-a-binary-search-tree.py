# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        
        self.dfs(root, val)
        return root
    
    def dfs(self, root, val):
        if not root:
            node = TreeNode(val)
            return node
        
        if root.val > val:
            root.left = self.dfs(root.left, val)
        else:
            root.right = self.dfs(root.right, val)
        
        return root