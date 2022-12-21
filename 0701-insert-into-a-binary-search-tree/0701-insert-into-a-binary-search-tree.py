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
        self.dfs(root, val, None, False)
        return root
    
    def dfs(self, root, val, father, is_left_child):
        if not root:
            node = TreeNode(val)
            if father and is_left_child:
                father.left = node
                return
            if father and not is_left_child:
                father.right = node
                return
        
        if root.val > val:
            self.dfs(root.left, val, root, True)
        else:
            self.dfs(root.right, val, root, False)
            