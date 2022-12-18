# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # inorder traversal, get the kth element
        stack = []
        curr = root
        idx = 0
        
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            idx += 1
            
            if idx == k:
                return curr.val
            if curr.right:
                curr = curr.right
            else:
                curr = None
        
        
            
            