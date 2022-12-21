# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        node_count = 0
        curr = root
        stack = []
        
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
                
            curr = stack.pop()
            node_count += 1
            
            if node_count == k:
                return curr.val
            if curr.right:
                curr = curr.right
            else:
                curr = None
                