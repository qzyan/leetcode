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
        
        father = None
        curr = root
        while curr:
            father = curr
            if curr.val > val:
                curr = curr.left
            else:
                curr = curr.right
                
        if father.val < val:
            father.right = TreeNode(val)
        else:
            father.left = TreeNode(val)
        
        return root